from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return("Hello, World! 🤍")

@app.route('/greeting')
def greetThis():
    return render_template('index.html', name="CHEESE BAGS")

pie_recipe = {
    'name': 'cheesecake',
    'ingredients': ['graham crackers', 'cream cheese', 'sugar']
}

@app.route('/pie')
def andThisPie():
    return jsonify({'pie ingredient': pie_recipe['ingredients'][0]})

@app.route('/recipe')
def forAllThosePies():
    return render_template('recipe.html', recipe=pie_recipe)

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
