from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    _tablename_ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    role = db.relationship('Role', back_populates='user')
    
    
    def _repr_(self):
        return f'<User {self.user_id}, {self.name}, {self.email}, {self.role}>'
    
class Role(db.Model):
    _tablename_ = 'roles'
    
    role_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    
    
    user = db.relationship('User', back_populates='role')
    
    def _repr_(self):
        return f'<Role {self.role_id}, {self.role}>'