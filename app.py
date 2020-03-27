from flask import Flask, render_template, jsonify, request
import random

app=Flask(__name__)

ingredients = ["apples", "sugar", "flour", "cinnamon", "honey"]



@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/greeting')
def greeting():
    name = "Santiago Camilo Davis"
    return render_template('index.html', name=name)

@app.route('/pie', methods=["POST","GET"])
def pie():
    if request.method == "POST":
        global ingredients
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)
        print(ingredients)

        index = random.randint(0, len(ingredient) -1)
        return jsonify({"pie ingredient": ingredients[index]})
    else:
        return render_template("pieForm.html")
    # return jsonify({'pie ingredient': ingredients[randint(0,4)]})