from flask import Flask, jsonify, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home():
    return("Hello Sam, it's the Home Page!")

# @app.route('/greeting/<name>')
@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Akilah')

# @app.route('/recipe')
# def ingredients():
#     return jsonify({'recipe for Sam': ingredients[0]})

ingredients = ['SWEG', 'DRIP', 'If your name starts with an S']

@app.route('/recipe', methods = ["GET", "POST"])
def new_ingredient():
    if request.method == "POST":
        new_ingredient = request.form["new_ingredient"]
        ingredients.append(new_ingredient)
        return redirect('/recipe')
        
    return render_template('recipe.html', ingredients = ingredients)



if __name__ == '__main__':
    app.run()