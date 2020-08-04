from flask import Flask, render_template, jsonify, redirect, request
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', name=name)

ingredients = ['blueberries', 'apple', 'peach']

    

@app.route('/pie', methods=['GET', 'POST'])
def ingredient():
    global ingredients

    if request.method == 'POST':
        new_ingredient = request.form['ingredient']
        ingredients.append(ingredient)
        return f"{ingredients}"
    else: 
        #get random index number from list length
        index = random.randint(0, (len(ingredients) -1))
        return render_template("pie_form.html", ingredient=ingredients[index])
    
        