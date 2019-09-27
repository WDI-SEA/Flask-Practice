#import stuff
import random
from flask import Flask, render_template
from blueprints.recipes import recipe_blueprint

#declare app
app = Flask(__name__)

#home route
@app.route('/')
def home():
    return render_template('index.html', name='Akilah')

@app.route('/greeting')
def greeting():
    return 'Hey'

@app.route('/pie')
def pie():
    ingredients = ['cream', 'filling', 'pecan']
    return 'Nothing'

#blueprints
app.register_blueprint(recipe_blueprint)

if __name__ == '__main__':
    app.run()