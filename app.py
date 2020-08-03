from flask import Flask, render_template, jsonify
app = Flask(__name__)
import random


@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/greeting')
def greeting():
  return render_template('index.html', name='Andrew')

@app.route('/pie')
def random_ingredient():
  ingredients = ['custard', 'peach', 'apple']
  return jsonify({'pie ingredient': random.choice(ingredients)})