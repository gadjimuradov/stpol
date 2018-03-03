import os
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.models import Work, Team
from app.forms import WorkForm, TeamForm
from app import app, db

UPLOAD_FOLDER = '/static/img/content'

@app.route('/')
@app.route('/index')
def index():
    last_works = Work.query.all()
    team = Team.query.all()
    return render_template('main.html', works=last_works, team=team)


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
        file = request.files['image_url']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        work.image_url = filename
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


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/technology')
def technology():
    return render_template('technology.html')




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


@app.route('/team/add', methods=['GET','POST'])
def add_team():
    form = TeamForm(request.form)

    if form.validate_on_submit():
        team = Team()
        team.fio = form.fio.data
        file = request.files['avatar']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        team.avatar = filename
        db.session.add(team)
        db.session.commit()
        return redirect('/')
    return render_template('add_team.html', form=form)


@app.route('/team/delete/<pk>/')
def delete_team(pk):
    team = Team.query.filter_by(id=pk).first()
    if team:
        db.session.delete(team)
        db.session.commit()

    return redirect('/')