import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/greeting')
def greeting():
    name = 'Nick'
    return render_template('index.html', name=name)

@app.route('/pie')
def pie():
    ingredients = ['sugar', 'spice', 'everything nice']
    {'pie_ingredient': ingredients}
    return jsonify({'pie_ingredient': ingredients[random.randint(0,3)]})

if __name__ == '__main__':
    app.run(port=3000, debug=True)