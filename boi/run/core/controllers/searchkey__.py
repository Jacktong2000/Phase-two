#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('key', __name__, url_prefix='/key')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('key.html')

