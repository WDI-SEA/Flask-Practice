from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
  return  "Hello World"

@app.route('/greeting')
def greetings():
  return "Hello, Peeps."

@app.route('/greeting/<name>')
def greeting(name):
  return render_template('greeting.html', name=name)

ingredients = ["Flour", "Butter", "Apples", "Sugar"]

@app.route('/pie')
def pie():
  global ingredients
  return jsonify({"ingredients": ingredients})

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
  global ingredients
  