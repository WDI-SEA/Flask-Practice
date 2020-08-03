from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/greeting')
def greeting():
    return render_template('greeting.html', name='Akilah')