from flask import Flask, render_template, jsonify, request, redirect

app=Flask(__name__)

@app.route('/')
def hello_world_of_pie():
    return "Hello, vast world of pie!"

@app.route('/greeting')
def greetings():
    name = "Akilah"
    return render_template('index.html', name=name)

ingredients = ["custard", "chocolate", "butter"]

@app.route('/pie')
def pie_pie():
    return jsonify({'pie ingredient' : ingredients[0]})

@app.route('/recipe', methods=["POST", "GET"])
def recipe_data():
    if request.method == "GET":
        return render_template('pie.html', name="Custard Pie")
    else:
        form_data = ingredients.append(ingredients)
        return redirect('/recipe')
