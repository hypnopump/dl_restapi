from app import app, db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    user = db.Column(db.String(50))

    def __init__(self, name, user):
        self.name = name
        self.user = user

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)
    user = db.Column(db.String(50))
    score = db.Column(db.Integer)
    img_id = db.Column(db.Integer)
    img_name = db.Column(db.String(150))

    def __init__(self, text, user, score, img_id, img_name):
        self.text = text
        self.user = user
        self.score = score
        self.img_id = img_id
        self.img_name = img_name
