from flask import Flask, request, render_template, jsonify
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"


ingredients = ["flour", "apples", "butter", "sugar"]

@app.route("/pie", methods=["GET", "POST"])
def ingredient():
    global ingredients

    if request.method == "POST":
        new_ingredient = request.form["ingredient"]
        ingredients.append(new_ingredient)
        return f"{ingredients}"
    else: 
        index = random.randint(0, (len(ingredients)-1))
        return render_template("ingredientsForm.html", ingredient=ingredients[index])