from flask import render_template, request, Blueprint,jsonify,json
from camsuapp.regions.forms import RegionForm
from camsuapp import db
from camsuapp.models import Branche
from pprint import pprint
regions = Blueprint('regions', __name__)


@regions.route("/region/manager",methods=['GET','POST'])
def region_home():
    form = RegionForm()
    branches =  Branche.query.all()
    return render_template('regions/region_manager.html',title='Gestion regions',form=form,branches=branches)

@regions.route("/region/add",methods=['GET','POST'])
def region_add():
    form= RegionForm()
    branche = Branche()
    '''branche.name_branche= request.form['branche']
    branche.name_siege = request.form['siege']
    branche.vile_local = request.form['ville']
    branche.name_president = request.form['amir']
    branche.annee_creation = request.form['date']
    branche.sous_branche = request.form['nombre']'''
    #return jsonify(branche)
    #db.session.add(branche)
    #db.session.commit()
    if form.validate_on_submit():
        return jsonify(data={'message': 'sucess' })
    return jsonify(errors=form.errors)

    
    
   
