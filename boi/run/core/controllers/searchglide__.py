#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('glide', __name__, url_prefix='/glide')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('glide.html')

