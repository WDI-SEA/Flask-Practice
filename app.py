#import stuff
from flask import Flask, render_template

#declare app
app = Flask(__name__)

#home route
@app.route('/')
def home():
    return render_template('index.html', name='Akilah')

if __name__ == '__main__':
    app.run()