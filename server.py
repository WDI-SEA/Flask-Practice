from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def sayHello():
    return "hello World"
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/pie', methods=['GET'])
def pie():
    ingredients =['apples', 'sugar', 'flour', 'allspice', 'butter']
    return jsonify({'pie ingredient': ingredients[0]})

if __name__ == "__main__":
    app.run()