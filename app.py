from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('index.html', name=name)