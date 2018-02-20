from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')


@app.route('/works', methods=['GET'])
def works():
    print("works")
    return render_template('works.html')