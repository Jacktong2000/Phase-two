#! /usr/bin/env/ python3

from flask import Blueprint, render_template, request, redirect, url_for, g, session

controller = Blueprint('general', __name__, url_prefix='')

@controller.route('/', methods=['GET','POST'])
def show_frontpage():
    if request.method == 'POST':
        session.pop('username', None)
        if request.form['username'] == 'victor' and request.form['password'] == 'frank':
            session['username'] = request.form['username']
            return redirect(url_for('general.login'))
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

@controller.route('/home', methods=['GET','POST'])
def login():
    return render_template('hahahalogin.html')


@controller.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@controller.route('/hahahalogout')
def logout():
    session.pop('username', None)
    return redirect(url_for('general.show_frontpage'))
