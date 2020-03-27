from flask import Flask, render_template, request, jsonify
import random

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/greeting')
def greeting():
    name = "Leif Eriksson"
    greeting = "Ahoy"
    return render_template('index.html', name=name, greeting=greeting)

ingredients = [
    'apples',
    'sugar',
    'flour'
]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    if request.method == 'POST':
        global ingredients

        #add submitted user ingredient to existing list
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)
        print(ingredients)

        # call random index
        index = random.randint(0, (len(ingredients)-1))

        return jsonify({'pie ingredients': ingredients, 'random ingredient': ingredients[index]})
    else:
        return render_template('pieform.html')
