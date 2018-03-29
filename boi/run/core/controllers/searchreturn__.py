#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('return', __name__, url_prefix='/return')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('return.html')

