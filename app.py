import random
from flask import Flask, render_template, jsonify, redirect, request, url_for
app = Flask(__name__)

# Render a home page that sends the string "Hello World"
@app.route('/', methods=['GET'])
def home():
    return "Hello World"

# Pass a name variable to a template that renders a personalized greeting
@app.route('/greeting', methods=['GET'])
def greeting():
    return render_template('index.html', name='Akilah')

# Return a JSON object that contains a key-value pair
@app.route('/pie', methods=['GET'])
def pie():
    ingredients = list(['Apples','Sugar','Flour','Pie Tin'])
    return jsonify({'pie ingredient': ingredients[random.randrange(len(ingredients))]})

# Return a list of ingredients and allow the user to add more
recipes = {
    'pie': ['Apples','Sugar','Flour','Pie Tin']
}
@app.route('/recipe', methods=['GET','POST'])
def recipe():
    if request.method == 'POST':
        recipes['pie'].append(request.form['newIngredient'])
        return redirect(url_for('recipe'))
    else:
        return render_template('recipe.html', recipe='pie', ingredients=recipes['pie'] )