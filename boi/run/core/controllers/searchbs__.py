#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('bs', __name__, url_prefix='/bs')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('bs.html')

