#! /usr/bin/env/ python3

from flask import Blueprint, render_template, request, redirect, url_for

controller = Blueprint('general', __name__, url_prefix='')

@controller.route('/', methods=['GET','POST'])
def show_frontpage():
    if request.method == 'POST':
        if request.form['username'] == 'victor' and request.form['password'] == 'frank':
            return redirect(url_for('general.login'))
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

@controller.route('/home', methods=['GET','POST'])
def login():
    return render_template('hahahalogin.html')
