from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Hello World! 🌎'


@app.route('/greeting')
def greeting():
    return render_template('index.html', value='Jamo')


pies = [
    {
        'flavor': 'Chocolate',
        'type': 'Cream'
    },
    {
        'flavor': 'Banana',
        'type': 'Cream'
    },
    {
        'flavor': 'Cherry',
        'type': 'Cobbler'
    },
    {
        'flavor': 'Peach',
        'type': 'Cobbler'
    }
]


@app.route('/pie')
def get_pie():
    for pie in pies:
        return jsonify(pie)


@app.route('/pies')
def get_pies():
    return jsonify(pies)


if __name__ == "__main__":
    app.run(port=5000)
