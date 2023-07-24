#!/usr/bin/env/python3

from flask import Flask

''' Create application instance'''
app = Flask(__name__)

''' Add route decorator'''
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/variabletest/<name>')
def print_variable(name):
    return 'Hello %s' % name

@app.route('/integertest/<int:intID>')
def print_integer(intID):
    return 'Number: %d' % intID

@app.route('/floattest/<float:floatID>')
def print_floatid(floatID):
    return 'Floating number: %f' % floatID


if __name__ == '__main__':
    app.run()
