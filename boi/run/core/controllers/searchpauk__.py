#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('pauk', __name__, url_prefix='/pauk')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('pauk.html')

