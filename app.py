from flask import Flask, jsonify, render_template, redirect, request

app = Flask(__name__)

ingredients = ['Apples', 'Cinnamon', 'Sugar']

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/greeting')
def greeting():
    my_name = 'David'
    return render_template('index.html', my_name=my_name) 

@app.route('/pie', methods=('GET', 'POST'))
def pie():
    return jsonify({'pie ingredient': ingredients[0]})

@app.route('/recipe', methods=('GET', 'POST'))
def recipe():
    if request.method == 'GET':
        return render_template('recipe.html', ingredients=ingredients)
    elif request.method == 'POST':
        ingredients.append(request.form['ingredient'])
        return redirect('/recipe')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
