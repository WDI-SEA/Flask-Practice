from flask import Flask, render_template, jsonify, redirect, request
import random
app = Flask(__name__)


ingredients = ["apples", "flour", "sugar", "love"]

@app.route('/')
def Hello():
    return 'Hello World 👋🏼🌍'


@app.route('/greeting/<name>')
def Greeting(name):
    return render_template('greeting.html', name=name)


@app.route('/pie')
def Ingrediets():
    global ingredients
    return jsonify({'pie ingredient': random.choice(ingredients) })


@app.route('/recipe', methods=['GET', 'POST'])
def Recipe():
    if request.method == 'POST':
        new_ingredient = request.form["ingredient"]
        ingredients.append(new_ingredient)
        return redirect('/recipe')
    else:
        
        return render_template('recipe.html', ingredients )

