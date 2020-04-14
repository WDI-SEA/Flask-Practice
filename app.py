from flask import Flask, render_template, jsonify, request, redirect
import random

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/greeting')
def greeting():
    name = "Shawhien"
    return render_template('index.html', name=name)

# Class Solution doing with bonus in consideration

ingredients = ['Apple', 'Eggs', 'Crust']

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    if request.method == 'POST':
        global ingredients
        ingredient = request.form['ingredient']
        ingredients.append(ingredient)
        print(ingredients)

        index = random.randint(0, (len(ingredients)-1))

        return jsonify({'pie ingredient': ingredients[index]})

    else:
            return render_template('pieForm.html')