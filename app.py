from flask import Flask, render_template, jsonify, redirect, request

app=Flask(__name__)

@app.route('/')
def hello():
  return "Hello World"

@app.route('/greeting')
def greeting():
  return render_template('index.html', name='Akilah')

ingredients = ['apples', 'pears', 'pecans']
pies = []
for ingredient in ingredients:
  pies.append({'pie ingredient': ingredient})
names=['Maximum Pie']

@app.route('/pie')
def pie():
  return jsonify(pies)

@app.route('/recipe', methods=["GET", "POST"])
def recipe():
  if request.method == "GET":
    ing_1=pies[-3]['pie ingredient']
    ing_3=pies[-1]['pie ingredient']
    ing_2=pies[-2]['pie ingredient']
    return render_template('recipe.html', name=names[-1], ingredient_1=ing_1, ingredient_2=ing_2, ingredient_3=ing_3)
  elif request.method == "POST":
    pies.append({'pie ingredient': request.form['ing_1']})
    pies.append({'pie ingredient': request.form['ing_2']})
    pies.append({'pie ingredient': request.form['ing_3']})
    names.append(request.form['name'])
    # ing_2 = request.form['ing_2']
    # ing_3 = request.form['ing_3']
    # new_ingredient = request.form["ingredient"]
    return redirect('/recipe')


# GET	/recipe	Render a template that shows the name of a pie, all ingredients, and a new ingredient form
# POST	/recipe	The form from the GET page sends a new ingredient. Add this to your ingredients list then redirect back to /recipe