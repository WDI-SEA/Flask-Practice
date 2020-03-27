from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def say_hello():
    return "Hello World"

@app.route('/greeting')
def greeting():
    name = "Akilah"
    return render_template('index.html', name=f'{name}')

@app.route('/pie')
def pie():
    recipes = {
        "pie": ['flour', 'eggs', 'sugar'],
        "pizza": ['flour', 'oil', 'water']
    }
    
    # return jsonify({'pie ingredient': recipes["pie"][0]})
    return jsonify({'pie ingredient': recipes["pie"]})