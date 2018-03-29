#! /usr/bin/env/ python3

from flask import Blueprint, render_template

controller = Blueprint('print', __name__, url_prefix='/print')

@controller.route('/', methods=['GET'])
def show_page():
    return render_template('print.html')

