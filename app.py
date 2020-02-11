# Import any needed packages including but not limited to flask
from flask import Flask, render_template, request
# Declare app instance
app = Flask(__name__)

# Declare routes
@app.route('/')
def home():
    return 'Hello World!'


# Get the server up and running
if __name__ == '__main__':
    app.run(debug=True)