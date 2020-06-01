from flask import Flask, render_template,jsonify,request
from random import randint
app = Flask(__name__)

#Problem 1: Hello World
@app.route("/")
def hello():
  return "Hello World!"

#Problem 2 :  Render Like Rembrandt and Problem 3: All I See is Static
@app.route("/greeting")
def index():
    return render_template("index.html", name='Akilah') 

# variation to print the name
@app.route("/greeting/<name>")
def greeting(name):
    return render_template("index.html", name=name) 

# Problem 4: A Detective, A PI
ingredients = ['apples','pineapple','mangoes']
@app.route("/pie")
def pie():
    return jsonify({'pie ingredient': ingredients[0]})    

# Bonus on Problem 4
ingredients = ['apples','pineapple','mangoes']
@app.route("/piee")
def pie_random():
    index = randint(0,2)
    return jsonify({'pie ingredient': ingredients[index]})     

# Bonus: The POST Man Deliverth
@app.route("/recipe", methods = ['POST', 'GET'])
def recipe():
    pie={'name':'Apple pie', 'ingredients' : ['flour','sugar']
            }
    pie_ingredient = ''        
    if request.method == 'POST':
      pie_ingredient = request.form['ingredient']
      print('pie_ingredient',pie_ingredient)
      pie['ingredients'].append(pie_ingredient)
    #else:
    return render_template("recipe.html", pie=pie) 


if __name__ == "__main__":
  app.run()