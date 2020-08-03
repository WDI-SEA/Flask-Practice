from flask import Flask, render_template, jsonify
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello, World!"

@app.route('/greeting/<name>')
def greeting(name):
  return render_template('index.html', name='Akilah')

ingredients = ["Peaches", "Brown Sugar", "Flour", "Salt", "Baking Soda", "Butter", "Vanilla", "Whiskey", "White Sugar", "Cinnamon"]

@app.route('/pie')
def pie():
  global ingredients
  random.shuffle(ingredients)
  return jsonify({'pie ingredient': ingredients[0]})