from flask import Flask, jsonify, render_template, request

app = Flask(__name__)



# home page
@app.route("/")
def home_route():
    return "Hello world"

# greeting route
@app.route('/greeting')
def greeting(name = 'Paul'):
    return render_template('/index.html', name = name)


ingredients = ['flour', 'apples', 'eggs']
#pie ingredients route
@app.route('/pie')
def pie():
    return jsonify({ 'pie ingredient': ingredients[0]})


# listen on port 5000
if __name__ == '__main__':
    app.run()
