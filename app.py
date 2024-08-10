import random
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)

# Simulate in-memory storage
data_store = {}

def process_data(item):
    if isinstance(item, str):
        return item.lower()
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

# API endpoint to fetch and process data
@app.route('/fetch-data', methods=['POST'])
def fetch_data():
    if not request.is_json:
        raise BadRequest('Request body must be JSON')

    mock_data = request.json.get('data', None)
    if mock_data is None:
        raise BadRequest('Missing "data" in request body')

    processed_data = process_data(mock_data)
    data_id = random.randint(1000, 9999)
    data_store[data_id] = processed_data

    return jsonify({'message': 'Data fetched and processed', 'data_id': data_id}), 201

# API endpoint to retrieve processed data
@app.route('/get-processed-data/<int:data_id>', methods=['GET'])
def get_processed_data(data_id):
    data = data_store.get(data_id)
    if data is None:
        raise NotFound('Data not found')

    return jsonify({'data_id': data_id, 'processed_data': data}), 200

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({'error': str(e)}), 400

@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
