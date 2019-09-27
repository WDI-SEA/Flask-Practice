from flask import Flask, render_template, request

# Declare app variable
app = Flask(__name__)

# Declare routes
@app.route("/")
def home_route():
    return "Hello world"

@app.route('/greeting')
def greeting(user = 'Kirk'):
    return render_template('/index.html', user = user)

# Listener
if __name__ == "__main__":
    app.run()