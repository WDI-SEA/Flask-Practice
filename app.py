from flask import Flask, redirect, render_template, jsonify, request
app = Flask(__name__)
import random



### ROUTES


#hello wolrd!
#GET /
@app.route('/test')
def hello_world():
    return 'HEY THAR'

#GET /greeting
@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', name = name)

#return a body with json data
#GET /api/testJSON
@app.route('/api/testJSON')
def getJSON():
    return jsonify([
        {'name':'Anna','role':'Teach the things'},{'name':'The King','role':'Teach the other things'}
        ])

ingredients = ["pie tin"]
@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    global ingredients
    if request.method =='POST':
        new_ingredient = request.form['ingredient']
        print(new_ingredient)
        ingredients.append(new_ingredient)
        redirect('/recipes')
    return render_template('recipes.html', ingredients = ingredients)

#GET /pie
#return a pie json object
@app.route('/pie')
def pie():
    randItem = ingredients.popitem()
    return jsonify(str(randItem))






###VARIABLES

#ingredients for pie builder form

# test ingredients object for GET /pie
sampleIngredients = ["merange", "apple", "cherry", "chocolate cream", "graham cracker crust"]



# {'filling0':'merangue','filling1':'apple','filling2':'cherry','filling3':'chocolate cream', 'shell1':'graham cracker','shell2':'oreo','shell3':'savory pastry'}