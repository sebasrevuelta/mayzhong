from werkzeug.wrappers import Request, Response

# Define a simple WSGI application
def application(environ, start_response):
    request = Request(environ)
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Access form data
        form_data = request.form
        # Extract specific form field values
        name = form_data.get('name', 'Anonymous')
        message = form_data.get('message', 'No message')
        
        # Prepare the response
        response_text = f"Name: {name}\nMessage: {message}"
        response = Response(response_text, mimetype='text/plain')
    else:
        # Display a simple HTML form
        response_text = '''
        <html>
            <body>
                <form method="POST" action="/">
                    Name: <input type="text" name="name"><br>
                    Message: <textarea name="message"></textarea><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
        '''
        response = Response(response_text, mimetype='text/html')
    
    # Return the response
    return response(environ, start_response)

# Run the application using Werkzeug's built-in server
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, application)
