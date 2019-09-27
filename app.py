# Import flask
from flask import Flask, render_template, jsonify 
import random

# flask instance
app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('greeting.html', name='Akilah')

@app.route('/pie')
def pie():
    ingredients = [
        'apples',
        'sugar',
        'cinnamon',
        'flour',
        'shortening'
    ]
    return jsonify({ 'pie ingredient': random.choice(ingredients) })

# Listen in port 5000
if __name__ == "__main__":
    app.run()