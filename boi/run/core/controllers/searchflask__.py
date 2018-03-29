#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('flask', __name__, url_prefix='/flask')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('flask.html')

