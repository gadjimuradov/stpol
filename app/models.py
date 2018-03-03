from app import db


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    youtube_url = db.Column(db.String(255))

    def __repr__(self):
        return '<Work {}>'.format(self.title)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(150))
    avatar = db.Column(db.String(255))

    def __repr__(self):
        return '<Team {}>'.format(self.fio)
