#import stuff
from flask import Flask

#declare app
app = Flask(__name__)

#home route
@app.route('/')
def home():
    return 'I guess this is it'

if __name__ == '__main__':
    app.run()