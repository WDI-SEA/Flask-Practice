from flask import Flask, render_template
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('index.html', name='Eric')


ingredients = ['apple', 'lychee', 'peach']
@app.route('/pie')
def pie():
    return jsonify({'pie ingredient': ingredients[0]})