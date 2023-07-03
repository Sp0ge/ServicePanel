from app.models import User, WebApps
from app.extentions import db
from flask import flash, render_template, Blueprint, redirect, url_for, request
from flask_wtf import FlaskForm
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import User_Add, User_log, WebApps_add
from sqlalchemy import func

index_bp = Blueprint("index", __name__, url_prefix="/")

@index_bp.before_request
def before_request():
    db.create_all()
    if current_user.is_anonymous and \
    str(request.endpoint) == "index.setup" and \
    len(User.query.all()) != 0:
        return redirect(url_for("index.log"))

@index_bp.route("/")
@index_bp.route("/index", methods=['GET','POST'])
def main():
    
    if len(User.query.all()) == 0:
        return redirect(url_for("index.setup"))
    else:
        services = WebApps.query.all()
        if request.method == "POST":
            name = str(request.form.get("search"))
            print(name)
            services = WebApps.query.filter(WebApps.title.ilike(f'%{name}%')).all()
            
        return render_template("index.html", services=services, user=current_user)

@index_bp.route("/app/add", methods=['GET','POST'])
@login_required
def app_add():
    form = WebApps_add()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        img_url = form.img_url.data
        url = form.url.data
        
        obj = WebApps(title=title,description=description,url=url,img_url=img_url)
        db.session.add(obj)
        db.session.commit()
        return redirect(url_for("index.main"))
    return render_template("app_add.html", form=form, user=current_user)

@index_bp.route("/app/del/<int:app>", methods=['GET','POST'])
@login_required
def app_del(app):
    obj = WebApps.query.get(app)
    db.session.delete(obj)
    db.session.commit()
    return redirect(url_for("index.main"))










@index_bp.route("/setup", methods=['GET','POST'])
def setup():
    form = User_Add()
    if form.validate_on_submit():
        user = form.username.data
        password = form.password.data
        obj = User(username=str(user))
        obj.set_password(str(password))
        db.session.add(obj)
        db.session.commit()
        return redirect(url_for("index.main"))
    return render_template("setup.html", form=form, user=current_user)

@index_bp.route("/app/settings/reset", methods=['GET','POST'])
def reset_all():
    database = WebApps.query.all()
    for obj in database:
        db.session.delete(obj)
    
    database = User.query.all()
    for obj in database:
        db.session.delete(obj)
    
    db.session.commit()
    return redirect(url_for("index.main"))

    
    
    
    
    
    
    
    
    
    
@index_bp.route("/auth/log", methods=['GET','POST'])
def log():
    if current_user.is_anonymous:
        form = User_log()
        if form.validate_on_submit():
            user = form.username.data
            password = form.password.data
            remember = form.remember_me.data
            obj = User.query.filter_by(username=user).first()
            if obj != None and obj.check_password(password) is True:
                print('login good')
                login_user(obj, remember)
                return redirect(url_for("index.main"))
            else:
                print('login error')
                flash("bad data")
            
        return render_template("log.html", form=form, user=current_user)
    else:
        return redirect(url_for("index.main"))
    
@index_bp.route("/auth/out", methods=['GET','POST'])
@login_required
def out():
    logout_user()
    return redirect(url_for('index.main'))
        