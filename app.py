from flask import Flask, jsonify, request, url_for, render_template, redirect, flash
from werkzeug.exceptions import BadRequest, NotFound
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Simulate in-memory storage
data_store = {}

def process_data(item):
    if isinstance(item, str):
        return item.upper()
    elif isinstance(item, (int, float)):
        return item * 2
    elif isinstance(item, list):
        if all(isinstance(sub_item, (int, float)) for sub_item in item):
            return sum(item)
        return [process_data(sub_item) for sub_item in item]
    elif isinstance(item, dict):
        return {key: process_data(value) for key, value in item.items()}
    else:
        return item

# Root route to list all available endpoints
@app.route('/')
def index():
    endpoints = {
        "Fetch Data": url_for('fetch_data', _external=True),
        "Get Processed Data": url_for('get_processed_data_view', _external=True),
    }
    return render_template('index.html', endpoints=endpoints)

# API endpoint to fetch and process data
@app.route('/fetch-data', methods=['GET', 'POST'])
def fetch_data():
    if request.method == 'POST':
        if not request.is_json and not request.form.get('data'):
            flash('Request body must be JSON or contain data in the form field', 'danger')
            return redirect(url_for('fetch_data'))

        data_input = request.json.get('data', None) if request.is_json else request.form.get('data')
        if data_input is None:
            flash('Missing "data" in request body or form', 'danger')
            return redirect(url_for('fetch_data'))

        try:
            mock_data = eval(data_input)
            processed_data = process_data(mock_data)
            data_id = random.randint(1000, 9999)
            data_store[data_id] = processed_data

            flash(f'Data fetched and processed with ID: {data_id}', 'success')
            return render_template('fetch_data.html', processed=True, data_id=data_id, data=processed_data)
        except Exception as e:
            flash(f'Error processing data: {str(e)}', 'danger')
            return redirect(url_for('fetch_data'))

    return render_template('fetch_data.html')

# API endpoint to retrieve processed data
@app.route('/get-processed-data', methods=['GET', 'POST'])
def get_processed_data_view():
    if request.method == 'POST':
        try:
            data_id = int(request.form.get('data_id'))
            return redirect(url_for('get_processed_data', data_id=data_id))
        except ValueError:
            flash('Invalid Data ID', 'danger')
            return redirect(url_for('get_processed_data_view'))
    
    return render_template('get_processed_data.html')

@app.route('/get-processed-data/<int:data_id>', methods=['GET'])
def get_processed_data(data_id):
    data = data_store.get(data_id)
    if data is None:
        flash('Data not found', 'danger')
        return redirect(url_for('get_processed_data_view'))

    return render_template('get_processed_data.html', data_id=data_id, data=data)

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({'error': str(e)}), 400

@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
