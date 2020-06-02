from flask import Flask, render_template, jsonify, redirect, request
import random
app = Flask(__name__)
app.config['DEBUG'] = True
ingredients = ['flour', 'eggs', 'sugar', 'butter', 'salt', 'apples']

@app.route('/')
def hello():
	return "Hello World"

@app.route('/greeting')
def greeting():
	return render_template('index.html', name='Akilah')

@app.route('/pie')
def pie():
	return jsonify({'pie ingredient': ingredients[random.randint(0,6)]})

@app.route('/recipe', methods = ['POST', 'GET'])
def recipe():
	if request.method == 'POST':
		new_ingredient = request.form['ingredient']
		ingredients.append(new_ingredient)
		return redirect('/recipe')
	else:
		return render_template('pie.html', ingredients = ingredients)

if __name__== "__main__":
	app.run(debug=True)