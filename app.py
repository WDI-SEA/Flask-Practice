import random

from flask import Flask
from flask import render_template
from flask import jsonify
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Akilah')

@app.route('/pie')
def pie():
    ingredients = ['apples', 'butter', 'sugar', 'flour',]
    random_number = random.randint(0, 3)
    return jsonify({'pie ingredient': ingredients[random_number]})    

if __name__ == '__main__':
    app.run()