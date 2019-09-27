from flask import Blueprint, render_template, request, redirect

recipe_blueprint = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipe_blueprint.route('/', methods=('GET'))
def index():
    return 'this is the end'