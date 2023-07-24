#!/usr/bin/env/python3

from flask import Flask, redirect, url_for

''' Create application instance'''
app = Flask(__name__)

''' Add route decorator'''
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/variabletest/<name>')
def print_variable(name):
    """
    function to show example instance
    :param name:
    :return:  Hello <name>
    """
    return 'Hello %s' % name

@app.route('/integertest/<int:intID>')
def print_integer(intID):
    return 'Number: %d' % intID

@app.route('/floattest/<float:floatID>')
def print_floatid(floatID):
    return 'Floating number: %f' % floatID

@app.route('/admin')
def hello_admin():
    return "Hello admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello % as guest" % guest

@app.route('/user/<user>')
def hello_user(user):
    if user == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = user))




if __name__ == '__main__':
    app.run()
