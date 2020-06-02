from flask import Flask, jsonify, redirect, render_template
from flask import request
app = Flask(__name__)

ingredients = ['apples', 'sugar', 'flour']
fuck = 'you'

app.config['DEBUG'] = True

###############Home Route###############
@app.route('/')
def hello():
    return "Hello World"
################Greeting################
@app.route('/greeting/<user>')
def greeting(user):
    return render_template('index.html', name = user)
###################API#######################
@app.route('/pie')
def pie():
    return jsonify({'pie ingredients': ['apples', 'sugar', 'flour']})

@app.route('/recipe', methods = ['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        ingredients.append(request.form['newnew']) 
        return redirect('/recipe')
    
    return render_template('recipe.html', value = ingredients)


if __name__ == "__main__":
    app.run()