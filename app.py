from flask import Flask, render_template, jsonify, request, url_for, redirect
import random
app =  Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
    return "Jello World!"


@app.route('/greeting', methods=['GET'])
def greeting():
    return render_template('index.html', name='Akilah')


@app.route('/pie', methods=['GET'])
def pie():
    ingredients = list(['Apples', 'Sugar', 'Pie Crust'])
    return jsonify({'pie ingredient': ingredients[0]})

recipes = {
    'pie': ['Apples', 'Sugar', 'Pie Crust' ]
}


@app.route('/recipe', methods=['GET','POST'])
def recipe():
    if request.method == 'POST':
        recipes['pie'].append(request.form['addIngredient'])
        return redirect(url_for('recipe'))
    else:
        return render_template('recipe.html', recipe='pie', ingredients=recipes['pie'] )




if __name__ == "__main__":
    app.run()
