from flask import render_template, request, Blueprint,jsonify,json
from camsuapp.regions.forms import RegionForm
from camsuapp import db
from camsuapp.models import Branche
from pprint import pprint
membres = Blueprint('membres', __name__)


@membres.route("/membre/manager")
def membre_home():
    return render_template('membres/membre_manager.html',title='Gestion membres')

   
