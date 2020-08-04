from flask import Flask, render_template, jsonify
import random
app = Flask (__name__)



@app.route('/')
def hello_world():
    return "Hello, World  🌎 "


@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Akilah')

ingredients = ["Flour", "Butter", "Sugar", "Apples"]

@app.route('/pie', method=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'POST':
        # get user input for ingredient and apped to ingredients
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)
        # get a random number between 0-length of list and set to index
        index = random.randint(0, (len(ingredients) - 1))

        # return a json object with random pie ingredients
        return jsonify({'pie ingredient': ingredients[0]})
    else:
        return render_template('pieForm.html')
