from flask import Flask, render_template, jsonify
app = Flask(__name__)
import random

  ingredients = ['custard', 'peach', 'apple']

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/greeting')
def greeting():
  return render_template('index.html', name='Andrew')

@app.route('/pie')
def random_ingredient():
  return jsonify({'pie ingredient': random.choice(ingredients)})
