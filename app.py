from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World 🌎"

@app.route('/greeting')
def hellooooo():
    return "helloooooooooooooooo"

# pass a name variable to a template that renders a personalized greeting
@app.route('/greeting/<name>')
def greeting(name):
    return render_template('index.html', name=name)


# # return a JSON object that contains a key-value pair
ingredients = ["apple", "cherry", "banana cream", "oreo", "vanilla custard", "chokeberry", "peach", "rhubarb"]

@app.route('/pie', methods=["GET", "POST"])

def make_pie():
    global ingredients
    if request.method == "POST":

        new_ingredient = request.form('ingredient')

        ingredients.append(new_ingredient)

        return f"{ingredients}"
    else:
        import random
        # apparently computers can't return a truly random integer

        index = random.randint(0, (len(ingredients) -1))

        return render_template("recipe.html", ingredient=ingredients[index])






