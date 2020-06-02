from flask import Flask, render_template, jsonify, redirect, request

app = Flask(__name__)
app.config['DEBUG']  = True
ingredients = ['salt', 'pepper', 'butter', 'water', 'avacadoes']

@app.route('/')
def hello():
    return "Hello World"

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Akilah')

@app.route('/pie')
def pie():
    return jsonify({'pie ingredient': ingredients[0]})

@app.route('/recipe', methods = ["GET","POST"])
def recipe():
    if request.method == 'POST':
        new_ingredients = request.form["ingredient"]
        ingredients.append(new_ingredients)
        return redirect('/recipe')
    else:
        return render_template('recipe.html', ingredients = ingredients)