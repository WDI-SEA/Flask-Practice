from flask import Flask, render_template, jsonify, request
import random

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/greeting')
def greeting():
    return render_template('index.html')


ingredients = ["Crust", "Brown Sugar", "Apples"]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'POST':
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)

        index = random.randint(0, (len(ingredients) - 1))
            return jsonify({'ingredient': ingredients[index]})
    else:
        return render_template('pieForm.html')