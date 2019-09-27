from flask import Blueprint, render_template, request

greeting_blueprint = Blueprint('greeting', __name__, url_prefix='/greeting')

@greeting_blueprint.route('/', methods=("GET", "POST"))
def index(): 
    if request.method =='GET': 
        return render_template('greeting.html', name="Akilah")