from datetime import datetime
from itsdangerous import JSONWebSignatureSerializer as Serializer
from camsuapp import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usr(user_id):
    return User.query.get(int(user_id))

particip_seminaires = db.Table('particip_seminaires',
db.Column('seminaire_id',db.Integer,db.ForeignKey('seminaires.id')),
db.Column('membre_id',db.Integer, db.ForeignKey('membres.id'))
) 
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(60),nullable=False)
    #fonction de user
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.password}')"
        
class Membre(db.Model):
    __tablename__ = 'membres'
    id = db.Column(db.Integer, primary_key=True)
    nom_prenom = db.Column(db.String(70), nullable=False)
    id_branche = db.Column(db.Integer,db.ForeignKey('branches.id'),nullable=False)
    qualite = db.Column(db.String(50), nullable=False)
    #ici le sexe sera un boolean , 1 pour masculin et 0 pour feminin
    sexe = db.Column(db.Boolean, default=False)
    etablissement = db.Column(db.String(50), default='aucun etablissement')
    email = db.Column(db.String(120),default="pas de email")
    annee = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    numero = db.Column(db.Integer, nullable=False, default=0)
    def __repr__(self):
        return f"Membre('{self.nom_prenom}','{self.qualite}')"  
class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    statut_permission=db.Column(db.Boolean, default=False)

class Branche(db.Model):
    __tablename__ = 'branches'
    id = db.Column(db.Integer, primary_key=True)
    name_branche = db.Column(db.String(45), nullable=False)
    name_siege = db.Column(db.String(45), nullable=False)
    vile_local = db.Column(db.String(45), nullable=False)
    name_president = db.Column(db.String(45), default='')
    annee_creation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sous_branche = db.Column(db.Integer, default=1)
    membres = db.relationship('Membre', backref='member',lazy=True)
    def __repr__(self):
        return f"Branche('{self.name_branche}','{self.name_siege}')"



class Seminaire(db.Model):
    __tablename__='seminaires'
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.Text, nullable= False)
    region_hote = db.Column(db.String(50), nullable=False)
    site = db.Column(db.String(50), nullable=False)
    cour_nom = db.Column(db.String(50), nullable=False)
    periode = db.Column(db.String(50), nullable=False)
    date_seminaire = db.Column(db.DateTime, nullable=False)
    membres= db.relationship('Membre',secondary=particip_seminaires,backref=db.backref('seminaires', lazy='dynamic'))
    def __repr__(self):
        return f"Seminaire('{self.theme}','{self.region_hote}')"

  





