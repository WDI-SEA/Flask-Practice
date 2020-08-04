from flask import Flask, render_template, jsonify, request, url_for
app = Flask(__name__)
import random



@app.route('/')
def hello_world():
  return '🤩Hello, world!'

@app.route('/greeting/<name>')
def rembrandt(name):
  return render_template('index.html', name=name)

ingredients = ['apples', 'sugar', 'flour', 'cinnamon']

@app.route('/pie', methods=['GET', 'POST'])
def getIngredient():
  global ingredients

  if request.method == 'POST':
    new_ingredient = request.form['ingredient']
    ingredients.append(new_ingredient)
    return f"{ingredients}"
  
  else:
    index = random.randint(0, (len(ingredients) - 1))
    # return jsonify({'pie ingredient': random.choice(ingredients)})

  return render_template("ingredientsForm.html", ingredient=ingredients[index])

# ingredients = ['apples', 'sugar', 'flour', 'cinnamon']
# @app.route('/recipe')
# def showPieRecipe():
#   name = 'apple'
#   return jsonify({name}':' {ingredients})

