# Import any needed packages including but not limited to flask
from flask import Flask, render_template, request, jsonify
import random
# Declare app instance
app = Flask(__name__)

# Declare routes
@app.route('/')
def home():
    return 'Hello World!'

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Akilah')

@app.route('/pie', methods=["GET"])
def pie():
    ingredients = ['flour', 'sugar', 'filling']
    return jsonify({'pie ingredient': ingredients[random.randint(0,len(ingredients) - 1)]})


# Get the server up and running
if __name__ == '__main__':
    app.run(debug=True)