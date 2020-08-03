from flask import Flask, render_template, jsonify
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '👋 hello world'

@app.route('/greeting')
def greeting():
  return render_template('index.html', name='Akilah')



@app.route('/pie')
def pie():d
  ingredients = ["apples", "sugar", "cinnamon"]
  return jsonify('pie ingredient:', random.choice(ingredients))