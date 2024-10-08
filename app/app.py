"""
This module handles the web application's main routes and logic.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Returns a greeting message."""
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
