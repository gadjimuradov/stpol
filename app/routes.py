import os
from flask import render_template, request, redirect, url_for
from app.models import Work
from app.forms import WorkForm
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    last_works = Work.query.all()
    return render_template('main.html', works=last_works)


@app.route('/works', methods=['GET'])
def works():
    works = Work.query.all()
    print(works)
    return render_template('works.html', works=works)


@app.route('/works/<pk>/')
def work_page(pk):
    work = Work.query.get(pk)
    return render_template('work_page.html', work=work)


@app.route('/works/add', methods=['GET','POST'])
def add_work():
    form = WorkForm(request.form)

    if form.validate_on_submit():
        work = Work()
        work.title = form.title.data
        work.youtube_url = form.youtube_url.data
        work.image_url = form.image_url.data
        work.body = form.body.data
        db.session.add(work)
        db.session.commit()
        return redirect('/works')
    return render_template('add_work.html', form=form)


@app.route('/works/delete/<pk>/')
def delete_work(pk):
    work = Work.query.filter_by(id=pk).first()
    if work:
        db.session.delete(work)
        db.session.commit()

    return redirect('/works')


@app.route('/test')
def test_page():
    return render_template('test.html')


@app.route('/qa')
def qa_page():
    return render_template('qa_page.html')


@app.route('/upload_insta_photo')
def upload_insta_photo():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    photo_path = base_dir + '/static/img/content/work6.jpg'
    # from InstagramAPI import InstagramAPI
    # InstagramAPI = InstagramAPI("dagstyazhka", "gmayunus2018")
    # InstagramAPI.login()
    # caption = "Выполним полусухую стяжку пола быстро и качественно"
    # InstagramAPI.uploadPhoto(photo_path, caption=caption)
    return 'Photo uploaded' + photo_path


@app.route('/insta/images')
def show_images_insta():
    return 'Images from insta'