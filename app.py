from flask import Flask, render_template, request, jsonify
import random

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world"

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Dylan')

ingredients = ['peaches', 'blueberries', 'crust']

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients 
    if request.method == 'POST':
# needs user inouts and add to ingredients 
        ingredient = request.form['ingredient']
        ingredients.append(ingredient)
#set index
        index = random.radiant(0, (len(ingredients) -1))
        return jsonify({'pie ingredient': ingredients[index]})
    else:
        return render_template('piePage.html')
    