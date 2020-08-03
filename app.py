from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! 🏈'

@app.route('/greeting')
def greetings():
    return 'Hello, American 🇺🇸'

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('index.html', name=name)


@app.route('/pie')
