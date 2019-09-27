from flask import Flask, render_template
from blueprints.greeting import greeting_blueprint

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template('index.html')

app.register_blueprint(greeting_blueprint)

if __name__ == '__main__': 
    app.run()