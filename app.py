from flask import Flask, render_template, jsonify

app = Flask(__name__)
ingredients = ['apple', 'flour', 'sugar']
@app.route('/')
def hello():
    return "hello world"

@app.route('/greeting')
def greeting():
   return render_template('index.html', name='David')

@app.route('/pie')
def pie():
   return jsonify({'pie ingredient': ingredients[0]})


if __name__ == "__main__":
    app.run()