from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True
# if using flask run, run in command line: export FLASK_DEBUG=0

# Routes
@app.route('/')
def hello():
    return "hello world!"

@app.route('/greeting')
def greeting():
   return render_template('index.html', name='Akilah')

@app.route('/pie')
def pie():
    ingredients = ['cayenne pepper', 'wheatgrass', 'apple cider vinegar', 'spirulina', 'açaí berries']
    return jsonify({'pie ingredient': ingredients[0]})


# __main__ is similar to the index.js in javascript/express
if __name__ == '__main__':
    app.run()
