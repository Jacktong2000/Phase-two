#!/usr/bin/env python3

import os

import importlib
from flask import Flask, session, g, redirect, url_for

from core.controllers.general import controller as general

from core.controllers.bicycle import controller as bicycle
#from core.controllers.amazon import controller as amazon


def keymaker(omnibus, filename='secret_key'):
    pathname = os.path.join(omnibus.instance_path, filename)
    try:
        omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()
    except IOError:
        parent_directory = os.path.dirname(pathname)
        if not os.path.isdir(parent_directory):
            os.system('mkdir -p {0}'.format(parent_directory))
        os.system('head -c 24 /dev/urandom > {0}'.format(pathname))
        omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()

with open('namespace2.txt') as f:
    usethis = []
    next(f)
    readthis = f.readlines()
    for i in readthis:
        addthis = 'search' + i.strip() + '__'
            #if '\n' in addthis:

        usethis.append(addthis)

for x in range(len(usethis)):
    out = usethis[x][6:]
    with open(os.path.join('run/core/templates','{temper}.html'.format(temper = out[:-2])), 'w') as f:
        f.write(out[:-2])

    with open(os.path.join('run/core/controllers', 'popo.py'), 'r') as f1:
        replacethis = f1.read()

    replacethis = replacethis.replace('replace', out[:-2])
    if '-' in out or '' in usethis[x]:
        into = usethis[x].replace('-', '_' )
        into = into.replace(' ', '_')
        with open(os.path.join('run/core/controllers','{temper}.py'.format(temper=into)), 'w') as f2:
            f2.write(replacethis)
    else:
        with open(os.path.join('run/core/controllers','{temper}.py'.format(temper=usethis[x])), 'w') as f2:
            f2.write(replacethis)


    with open(os.path.join('run/core/templates','hahahalogintemp.html'), 'a') as f3:
        f3.writelines('\n <a href="/{0}">{1}</a><br> \n'.format(out[:-2], out[:-2]))

    #from core.controllers.{} import controller as {}.format(out,out))
os.system('sort -u run/core/templates/hahahalogintemp.html > run/core/templates/hahahalogin.html')

for p in range(len(usethis)):
    out = usethis[p]
    if '-' in out or '' in out:
        out = out.replace('-', '_' )
        out = out.replace(' ', '_')
    o = exec('from core.controllers.{0} import controller as {1}'.format(out, out))
    o

omnibus = Flask(__name__)

omnibus.register_blueprint(general)
omnibus.register_blueprint(bicycle)

for q in range(len(usethis)):
    out = usethis[q]
    if '-' in out or '' in out:
        out = out.replace('-', '_' )
        out = out.replace(' ', '_')
    k = exec('omnibus.register_blueprint({0})'.format(out))
    k

keymaker(omnibus)

