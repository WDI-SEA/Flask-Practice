from flask import Flask

# Declare app variable
app = Flask(__name__)

# Declare routes
@app.route("/")
def home_route():
    return "Hello world"

# Listener
if __name__ == "__main__":
    app.run()