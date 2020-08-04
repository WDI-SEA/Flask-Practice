from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World 🌎"

@app.route('/greeting')
def hellooooo():
    return "helloooooooooooooooo"

# pass a name variable to a template that renders a personalized greeting
@app.route('/greeting/<name>')
def greeting(name):
    return render_template('index.html', name=name)

# # return a JSON object that contains a key-value pair
@app.route('/pie')
def make_pie():
    import random
    ingredients = ["apple", "cherry", "banana cream", "oreo", "vanilla custard", "chokeberry", "peach", "rhubarb"]
    return jsonify("your pie type: ", random.choice(ingredients))






