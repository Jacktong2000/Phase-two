#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('fly', __name__, url_prefix='/fly')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('fly.html')

