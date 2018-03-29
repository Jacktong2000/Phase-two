#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('numpy', __name__, url_prefix='/numpy')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('numpy.html')

