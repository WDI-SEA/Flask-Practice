from flask import Blueprint, render_template, request, jsonify

pie_blueprint = Blueprint('pie', __name__, url_prefix='/pie')

@pie_blueprint.route('/', methods=("GET", "POST"))
def index():
    ingredient = ['apples', 'strawberries', 'hampster'] 
    if request.method =='GET': 
        return jsonify({'pie ingredient': ingredient[0]})