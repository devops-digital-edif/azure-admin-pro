from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, User, Course, UserCourse
from .storage import upload_to_blob

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/admin/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        profile_pic = request.files['profile_pic']
        pic_url = upload_to_blob(profile_pic, 'profile-pictures')

        user = User(name=name, email=email, phone=phone, profile_picture_url=pic_url)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.home'))

    return render_template('admin/create_user.html')