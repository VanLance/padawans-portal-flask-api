from app import db

from werkzeug.security import generate_password_hash, check_password_hash



class UserModel(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password_hash = db.Column(db.String, nullable = False)
    first_name= db.Column(db.String(75))
    last_name= db.Column(db.String(75))

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def del_user(self):
        db.session.delete(self)
        db.session.commit()


