from flask import render_template,url_for,flash,redirect,request
#ici app represente le dossier app et non l'application app Flak (from app)
from app import app,db,bcrypt
from .forms import RegisterForm,LoginForm
from .models import User
from flask_login import login_user,current_user,logout_user,login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account create by success,your now login!' , 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html',title='Register',form=form)
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login unsuccefull','danger')
            return redirect('login')
    return render_template("auth/login.html",title="Login", form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    image_file = url_for('static',filename="profil_picture/" + current_user.image_user)
    return render_template('auth/account.html',image_file=image_file)



