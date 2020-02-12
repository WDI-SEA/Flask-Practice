#import packages
from flask import Flask, render_template, request, jsonify, redirect
import random

#declare app instance
app = Flask(__name__)


#global variables
ingredients = ['sugar', 'eggs', 'flour']

#routes
@app.route('/')
def home():
    return 'Hello World'

@app.route('/greeting')
def greeting():
    name = 'Kennan'
    return render_template('index.html', name=name )

@app.route('/recipe', methods=('POST', 'GET'))
def recipe():
    if request.method == 'GET':
        return render_template('recipe.html', ingredients=ingredients)
    elif request.method == 'POST':
        ingredients.append(request.form['ingredient'])
        return redirect('/recipe')

@app.route('/pie')
def pie():

    i = random.randint(0,2)
    return jsonify({'pie ingredient': ingredients[i]})

#run server
if __name__ == '__main__':
    app.run(port=5000, debug=True)