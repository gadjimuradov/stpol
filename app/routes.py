from flask import render_template, request, redirect, url_for
from app.models import Work
from app.forms import WorkForm
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')


@app.route('/works', methods=['GET'])
def works():
    works = Work.query.all()
    print(works)
    return render_template('works.html', works=works)


@app.route('/works/add', methods=['GET','POST'])
def add_work():
    form = WorkForm(request.form)

    if form.validate_on_submit():
        work = Work()
        work.title = form.title.data
        db.session.add(work)
        db.session.commit()
        return redirect('/works')
    return render_template('add_work.html', form=form)


@app.route('/test')
def test_page():
    return render_template('test.html')