from . import db

   

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(80))
    bio = db.Column(db.String(600))
    created_on = db.Column(db.String(12))
    photo = db.Column(db.String(80))
    

    
    def __init__(self,firstname,lastname,gender,email,location,bio,created_on,photo):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.created_on = created_on
        self.photo = photo
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def __repr__(self):
        return "User: {0} {1}".format(self.firstname, self.lastname)
