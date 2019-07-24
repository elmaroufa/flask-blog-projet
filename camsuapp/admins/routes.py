from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from camsuapp import db, bcrypt
from camsuapp.models import User

admins = Blueprint('admins', __name__)

@admins.route("/admin/home")
def home():
    return render_template('admin/admin.home.html')