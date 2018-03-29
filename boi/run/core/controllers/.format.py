#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('.format', __name__, url_prefix='/.format')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('.format.html')

