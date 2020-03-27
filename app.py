from flask import Flask, render_template, jsonify
from random import randint

app=Flask(__name__)

ingredients = ["apples", "sugar", "flour", "cinnamon", "honey"]



@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/greeting')
def greeting():
    return render_template('index.html', name="Santiago Camilo Davis")

@app.route('/pie', methods=["GET"])
def pie():
    return jsonify({'pie ingredient': ingredients[randint(0,4)]})