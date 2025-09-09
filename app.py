# app.py
from flask import Flask

# Create an instance of the Flask class.
# This is the main part of the application.
app = Flask(__name__)

# Define a route for the root URL ('/').
# When a user visits this URL, the 'hello_world' function will be executed.
@app.route('/')
def hello_world():
    """
    Returns a simple greeting message.
    """
    return 'Hello, VS Code!'

# This block ensures the application runs only when the script is executed directly.
# The 'debug=True' option enables a debugger and reloader for development.
if __name__ == '__main__':
    app.run(debug=True)
