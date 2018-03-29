#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('amazon', __name__, url_prefix='/amazon')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('amazon.html')

