from flask import Flask, jsonify, redirect, render_template, request
import random

app = Flask(__name__)

ingredients = ['apples', 'flour', 'butter', 'sugar', 'cinnamon', 'nutmeg']
recipe_name = 'Apple Pie'

@app.route('/')
def home():
    return "Hello World"

@app.route('/greeting')
def greeting():
    name = 'Will'
    return render_template('index.html', name=name)

@app.route('/pie', methods=['GET'])
def pie():    
    if request.method == 'GET':
        return jsonify({'pie ingredient': ingredients[random.randint(0, len(ingredients)-1)]})

@app.route('/recipe', methods=['GET', 'POST'])
def get_recipe():
    if request.method == 'GET':
        return render_template('recipe.html', recipe=recipe_name, ingredients=ingredients)
    elif request.method == 'POST':
        new_ingredient = request.form['ingredient']
        ingredients.append(new_ingredient)
        return redirect('/recipe')


if __name__ == '__main__':
    app.run(port=3001, debug=True)