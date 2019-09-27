from flask import Flask, render_template
from blueprints.greeting import greeting_blueprint
from blueprints.pie import pie_blueprint

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template('index.html')

app.register_blueprint(greeting_blueprint)
app.register_blueprint(pie_blueprint)

if __name__ == '__main__': 
    app.run()