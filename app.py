from flask import Flask, render_template, jsonify

app=Flask(__name__)

@app.route('/')
def hello_world_of_pie():
    return "Hello, vast world of pie!"

@app.route('/greeting')
def greetings():
    name = "Akilah"
    return render_template('index.html', name=name)

@app.route('/pie')
def pie_pie():
    ingredients = ["custard", "chocolate", "butter"]
    return jsonify({'pie ingredient' : ingredients[0]})

