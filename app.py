from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world"

@app.route('/owner')
def tell_owner():
    owner = "Anna"
    return render_template('index.html', owner=owner)