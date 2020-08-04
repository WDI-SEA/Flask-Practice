from flask import Flask, render_template, jsonify, request, redirect, url_for
import random
app = Flask(__name__)

@app.route('/')
def home():
    return("Hello, World! 🤍")

@app.route('/greeting')
def greetThis():
    return render_template('index.html', name=str("CHEESE BAGS"))

pie_recipe = {
    'name': 'cheesecake',
    'ingredients': ['graham crackers', 'cream cheese', 'sugar']
}

@app.route('/pie')
def andThisPie():
    return jsonify({'pie ingredient': random.choice(pie_recipe['ingredients'])})

@app.route('/recipe')
def forAllThosePies():
    return render_template('recipe.html', recipe=pie_recipe)

@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    global pie_recipe
    pie_recipe['ingredients'].append(request.form['new_ingredient'])
    print(f'ingredient added: {pie_recipe}')
    return redirect(url_for('forAllThosePies'))

class Pet():
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
    def walk(self):
        print(f'{self.name} needs a walk!')

spike = Pet("Milcah", "Spike")
spike.walk()

class Pup(Pet):
    def __init__(self, owner, name, loves):
        #Pet.__init__(owner, name) #maybe don't need 
        self.loves = loves
