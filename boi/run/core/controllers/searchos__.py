#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('os', __name__, url_prefix='/os')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('os.html')

