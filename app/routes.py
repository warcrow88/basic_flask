#
from app import app
# render_template is a function that when called, it will render on the browser the file passed in
from flask import render_template

# decorators
@app.route('/')
@app.route('/index')

def index():
    name = 'Max'
    num = 3
    names = ['conner', 'chet', 'fiona', 'todd', 'tara', 'tyler']
    return render_template('index.html', name=name, num=num, names=names)
