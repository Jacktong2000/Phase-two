#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('__init__', __name__, url_prefix='/__init__')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('__init__.html')

