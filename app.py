import random

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
app.config['DEBUG'] = True

ingredients = ['apples', 'butter', 'sugar', 'flour',]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Akilah')

@app.route('/pie')
def pie():
    random_number = random.randint(0, 3)
    return jsonify({'pie ingredient': ingredients[random_number]})    

@app.route('/recipe', methods = ['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        new_ingredient = request.form['new_ingredient']
        ingredients.append(new_ingredient)
        random_number = random.randint(0, len(ingredients))
        return render_template('recipe.html', ingredients = ingredients)  
    else:
        return render_template('recipe.html', ingredients = ingredients)  

if __name__ == '__main__':
    app.run()