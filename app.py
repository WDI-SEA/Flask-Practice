from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', name=name)

@app.route('/pie')
def pie():
    ingredients = "banana", "cream", "almond", "vanilla", "cinnamon"
    return jsonify({'pie ingredient': ingredients})