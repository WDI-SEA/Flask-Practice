from flask import Flask, render_template, request, jsonify
import random

# Declare app variable
app = Flask(__name__)

# Declare routes
@app.route("/")
def home_route():
    return "Hello world"

@app.route('/greeting')
def greeting(user = 'Kirk'):
    return render_template('/index.html', user = user)

@app.route('/pie')
def pie():
    return jsonify({ '"pie ingredient"': random.choice(pie_ingredients) })

pie_ingredients = ['flour', 'butter', 'eggs']


# Listener
if __name__ == "__main__":
    app.run()