from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('name.html', name=name)

ingredients = ["Crust, Applies, Sugar, Butter"]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        ingredients.push(ingredient)

        index = random.randint(0, (len(ingredients) -1))
        return jsonify({'pie ingredient': ingredients[index]})
else: 
    return render_template('pie.html')
    