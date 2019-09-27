# Import stuff
import random
from flask import Flask, render_template, request, jsonify

#Declare flask app instance
app = Flask(__name__)

#Home Page Route
@app.route("/")
def home_route():
    return "Hello world"

@app.route('/greeting')
def greeting(user = 'SHUKRI'):
    return render_template('/index.html', user = user)

@app.route('/pie')
def pie():
    return jsonify({ '"pie ingredient"': random.choice(pie_ingredients) })

pie_ingredients = ['sugar', 'spice', 'and', 'everything nice']


# Listener
if __name__ == "__main__":
    app.run()