from flask import Flask, render_template, jsonify, redirect, request
import random

app = Flask(__name__)

ingredients = ['apple', 'cherry', 'meat']
recipes = {
    'apple': ['apples', 'flour'],
    'cherry': ['cherries', 'flour'],
    'peach': ['peaches', 'flour']
}

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/greeting')
def greeting():
    return render_template('greeting.html', name='Akilah')

@app.route('/pie')
def pie():
    ingredient = random.choice(ingredients)
    return jsonify({'pie ingredient': ingredient})

@app.route('/recipe/<pie>', methods = ['GET', 'POST'])
def recipe(pie):
    if (request.method == 'GET'):
        for recipe in recipes:
            return render_template('recipe.html', name = pie, ingredients = recipes[pie])
    if (request.method == 'POST'):
        new_ingredient = request.form['ingredient']
        redirect_key = request.form['redirect']
        for recipe in recipes:
            recipes[pie].append(new_ingredient)
            return redirect(f'/recipe/{pie}')