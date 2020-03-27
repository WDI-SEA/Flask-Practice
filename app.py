from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def say_hello():
    return "Hello World"

@app.route('/greeting')
def greeting():
    name = "Akilah"
    return render_template('index.html', name=f'{name}')