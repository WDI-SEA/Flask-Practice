from flask import Flask, redirect, render_template, request, jsonify

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello World"

@app.route("/greeting")
def greeting():
    return render_template('index.html', name='Akilah')

@app.route("/pie")
def pie():
    ingredients=['apples', 'butter', 'sugar', 'flour']
    return jsonify({'pie ingredient': ingredients[0]})

ingredients=['apples', 'butter', 'sugar', 'flour', 'baking soda']
@app.route("/recipe", methods=['GET','POST'])
def recipe():
    if request.method == 'POST':
        new_ingredient = request.form["ingredient"]
        ingredients.append(new_ingredient)
        return redirect ('/recipe')
    else:
        return render_template('pie.html', name="apple pie", ingredients=ingredients)

if __name__ == "__main__":
    app.run()