from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)
app.config['DEBUG'] = True
# if using flask run, run in command line: export FLASK_DEBUG=0
ingredients = ['cayenne pepper', 'wheatgrass', 'apple cider vinegar', 'spirulina', 'açaí berries']

# Routes
@app.route('/')
def hello():
    return "hello world!"

@app.route('/greeting')
def greeting():
   return render_template('index.html', name='Akilah')

@app.route('/pie')
def pie():
    i = random.randint(0, (len(ingredients)-1))
    return jsonify({'pie ingredient': ingredients[i]})

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    if request.method=='POST':
        new_ingredient = request.form['poster']
        ingredients.append(new_ingredient)
        i = random.randint(0, (len(ingredients)-1))
        return render_template('pie.html', ingredients=ingredients)
    else:
        return render_template('pie.html', ingredients=ingredients)
# __main__ is similar to the index.js in javascript/express
if __name__ == '__main__':
    app.run()
