from flask import Flask, render_template, jsonify, redirect, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', name=name)

ingredients = ['blueberries', 'apple', 'peach']

@app.route('/pie',)
def pie():
    return jsonify({'pie ingredient': ingredients[0]})
    

@app.route('/recipe', methods=['GET', 'POST'])
def ingredient():
    global ingredients
    if request.method == 'POST':
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)
        return render_template('pie_form.html', ingredient=ingredient)
    else request.method == 'GET':
        return redirect('/recipe')
    
ingredient()
        