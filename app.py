from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/greeting')
def greeting():
    name = "Anna"
    greeting = "Hi"
    return render_template('index.html', name=name, greeting=greeting)

@app.route('/pie')
def pie():
    ingredients = [
        'apples',
        'sugar',
        'flour'
    ]
    return jsonify({'pie ingredient': ingredients[0]})