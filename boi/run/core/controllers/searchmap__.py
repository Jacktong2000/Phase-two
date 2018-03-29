#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('map', __name__, url_prefix='/map')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('map.html')

