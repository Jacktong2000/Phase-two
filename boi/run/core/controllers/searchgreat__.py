#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('great', __name__, url_prefix='/great')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('great.html')

