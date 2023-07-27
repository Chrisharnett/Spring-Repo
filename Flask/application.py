#!/usr/bin/env/python3

from flask import Flask, redirect, url_for, request, render_template

''' Create application instance'''
app = Flask(__name__)

''' Add route decorator'''
@app.route('/')
def hello_world():
    return render_template('base.html')

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
        return redirect(url_for('hello_guest', guest=user))

@app.route('/input.html', methods=['POST', 'GET'])
def information():
    if request.method == 'POST':
        info = request.form['info']
        return redirect(url_for('hello_guest', guest=info))
    else:
        return redirect(url_for('hello_world'))

@app.route('/texample')
def table_example():
    username = 'Michael'
    avg_score = 70
    marks_dict = {"Physics": 50, "Chem": 70, "Math": 90}
    return render_template('texample.html', name=username, marks=avg_score, results=marks_dict)


if __name__ == '__main__':
    app.run(debug=True)
