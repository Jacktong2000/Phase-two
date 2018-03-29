#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('lambda', __name__, url_prefix='/lambda')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('lambda.html')

