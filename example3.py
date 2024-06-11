# Import necessary packages from werkzeug and Flask
from werkzeug.wrappers import Request, Response
from flask import Flask, request

# Create a Flask application instance
app = Flask(__name__)

# Define a route that accepts POST requests
@app.route('/submit', methods=['POST'])
def submit_form():
    # Access the form data using request.form
    form_data = request.form
    # Extract specific form fields
    name = form_data.get('name')
    email = form_data.get('email')
    
    # Create a response using the extracted form data
    response = f"Received form data: Name - {name}, Email - {email}"
    return Response(response, content_type='text/plain')

# Define the main entry point for the application
if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
