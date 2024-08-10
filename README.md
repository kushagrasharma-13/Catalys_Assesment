# Catalys_Assesment

```markdown
# Flask Data Retrieval and Processing API

## Overview

This Flask application is designed to simulate a simplified data retrieval and processing system. It provides a user-friendly interface to interact with the API, allowing users to submit data for processing and retrieve processed results through a series of styled web pages.

### Features:
- **Home Page**: Lists all available API endpoints with links.
- **Fetch Data**: Allows users to submit data for processing (e.g., strings, numbers, lists, or dictionaries).
- **Get Processed Data**: Retrieve processed data by entering a specific data ID.

## Project Structure

```
.
├── app.py
├── templates
│   ├── index.html
│   ├── fetch_data.html
│   ├── get_processed_data.html
├── static
│   └── css
│       └── styles.css
└── requirements.txt
```

### File Descriptions:
- **`app.py`**: The main Flask application file containing all the routes and logic for processing and retrieving data.
- **`templates/`**: Contains all HTML templates used for rendering web pages.
  - **`index.html`**: The home page listing all available endpoints.
  - **`fetch_data.html`**: Page for submitting data to be processed.
  - **`get_processed_data.html`**: Page for retrieving processed data based on a data ID.
- **`static/css/styles.css`**: The custom CSS file used to style the web pages.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-directory>
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install the Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask Application**
   ```bash
   python app.py
   ```

2. **Access the Application**
   - Open your web browser and go to `http://127.0.0.1:5000/` to access the home page.

### API Endpoints

1. **Home Page**
   - **URL**: `http://127.0.0.1:5000/`
   - **Description**: Lists all available API endpoints with clickable links.

2. **Fetch Data**
   - **URL**: `http://127.0.0.1:5000/fetch-data`
   - **Methods**: `GET`, `POST`
   - **Description**: Submit data (e.g., strings, numbers, lists, or dictionaries) for processing.
   - **Input**: Data can be submitted as JSON (via API) or via an HTML form on the web page.
   - **Output**: Displays processed data and a unique data ID.

3. **Get Processed Data**
   - **URL**: `http://127.0.0.1:5000/get-processed-data`
   - **Methods**: `GET`, `POST`
   - **Description**: Retrieve processed data by entering a specific data ID.
   - **Input**: Enter the data ID via an HTML form.
   - **Output**: Displays the processed data associated with the entered ID.

## Customization

### CSS Styling
- The CSS file located at `static/css/styles.css` can be customized to modify the appearance of the web pages. The current styling includes:
  - A clean, modern layout using Bootstrap 4.
  - Custom background color and card shadow effects.
  - Hover effects for links.

### Templates
- The HTML templates in the `templates/` directory can be modified to customize the structure and content of each page. Each template is styled using Bootstrap and custom CSS.

## Conclusion

This Flask application provides a simple, styled interface for data processing and retrieval. It's easy to set up and run locally, making it a great starting point for building more complex data-driven applications. The consistent styling and user-friendly navigation make the application accessible and easy to use.
```

This README file is formatted in Markdown and is ready to be added to your repository. It includes all necessary information to help users understand, set up, and use the application effectively.