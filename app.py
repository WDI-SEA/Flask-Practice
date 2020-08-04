from flask import Flask, render_template, jsonify, request
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '<h1> Hello World </h1>'

@app.route('/<name>')
def name(name):
  return render_template('index.html', name=name)

ingredients = [
  'apples', 
  'sugar', 
  'ap flour', 
  'cinnamon', 
  'ginger', 
  'nutmeg', 
  'all-spice', 
  'rum', 
  'apple cider vinegar', 
  'salt', 
  'ice water', 
  'grandma\'s love'
]

@app.route('/pie')
def pie():
  # get random ingredient
  ingredients_length = len(ingredients)
  random_index = random.randrange(0, ingredients_length, 1)
  return jsonify({'pie ingredient': ingredients[random_index]})

pies = {
  'apple': ingredients
}

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
  # POST req from form
  if request.method == 'POST':
    # get pies object
    global pies
    # form input
    ingredient = request.form['ingredient']
    pie = request.form['pie']
    # check if the pie exists already or make it
    if pie in pies:
      pies[pie].append(ingredient)
    else:
      pies[pie] = [ingredient] 
    print(pies)
  # return pies for all requests
  return render_template('recipe.html', pies=pies)