from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/greeting')
def greeting():
    return render_template('index.html', name="Constance")


ingredients = ['Milk', 'Butter', 'Eggs', 'Flour', 'Ground beef', 'Potatoes']

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'POST':
        # add submitted user ingredient to existing list
        ingredient = request.form['ingredient']
        ingredients.append(ingredient)
        print(ingredients)

        random.shuffle(ingredients)
        for i in ingredients:
            return jsonify({'pie ingredient': i})

        # call random index
        # index = random.randint(0, (len(ingredients)-1))
        # return jsonify({'pie ingredient': ingredients[index]})
    else:
        return render_template('pie.html')

    # random.shuffle(ingredients)
    # for i in ingredients:
    #     return jsonify({'pie ingredient': i})
    
        