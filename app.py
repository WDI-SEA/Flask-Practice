from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
  return ('hello, world')

@app.route('/greeting')
def greeting():
  return render_template('index.html', name = 'Akilah')


@app.route('/pie')
def pie():
  ingredients = ['apples', 'butter', 'sugar']

  # {'pie ingredient': 'apples'}
  return jsonify({'pie ingredient': str(ingredients[0])})


if __name__ == '__main__':
  app.run()
