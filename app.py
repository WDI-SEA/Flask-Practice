from flask import Flask, render_template, jsonify
import random
import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! 🥝🥔'

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', name=name)

# create initial list of ingredients
ingredients = ["Flour", "Butter", "Apples"]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'POST':
        # get user input for ingredient and append to ingredients
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)

        # get a random number between 0-length of list and set to index
        index = random.randint(0, (len(ingredients) - 1))
    
        # return a json object with random pie ingredient
        return jsonify({'pie ingredient': ingredients[index]})
    else:
        return render_template('form.html')