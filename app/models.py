from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(15))
    profile_picture_url = db.Column(db.String(500))
    courses = db.relationship('UserCourse', back_populates='user')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    fee = db.Column(db.Float)
    duration = db.Column(db.String(50))
    image_url = db.Column(db.String(500))
    users = db.relationship('UserCourse', back_populates='course')

class UserCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    user = db.relationship('User', back_populates='courses')
    course = db.relationship('Course', back_populates='users')