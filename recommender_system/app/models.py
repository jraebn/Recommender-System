from app import db
from app import app
from sqlalchemy.orm import relationship



class Users(db.Model):
    __tablename__ = "Users"
    id= db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique =True)
    password = db.Column(db.String(255))
    location = db.Column(db.String(255))
    age = db.Column(db.Integer)
    ratings = relationship("Rating")
    
    def __init__(self,username,email,password,name, location,age):
        self.username = username
        self.email = email
        self.password = password
        self.name=name
        self.location = location
        self.age = age

    def __repr__(self):
        return '<User %r>' % self.username

class Books(db.Model):
    __tablename__ = "Books"
    isbn = db.Column(db.String(255), primary_key = True)
    booktitle = db.Column(db.String(255))
    bookauthor= db.Column(db.String(255))
    yrpublished = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    imgurl1 = db.Column(db.String(255))
    imgurl2 = db.Column(db.String(255))
    imgurl3 = db.Column(db.String(255))
    ratings = relationship("Rating")

    def __init__(self,isbn,bookauthor,booktitle,yrpublished,publisher,imgurl1,imgurl2,imgurl3):
        self.isbn = isbn
        self.booktitle = booktitle
        self.bookauthor = bookauthor
        self.yrpublished =yrpublished
        self.publisher = publisher
        self.imgurl3 = imgurl3
        self.imgurl2 = imgurl2
        self.imgurl1 =  imgurl1

    def __repr__(self):
        return '<ISBN %r>' % self.isbn

class Rating(db.Model):  
    __tablename__ = "Rating"
    ratingid = db.Column(db.Integer, primary_key =True)
    bookid = db.Column(db.String, db.ForeignKey('Books.isbn'))
    userid = db.Column(db.Integer, db.ForeignKey('Users.id'))
    stars = db.Column(db.Integer)
    comment = db.Column(db.String(1200))
    datepublished = db.Column(db.DateTime)
    
    def __init__(self, bookid, userid, stars, comment):
        self.bookid = bookid
        self.userid = userid
        self.stars = stars
        self.comment = comment
        self.datepublished = datetime.now()
    
    def __repr__(self):
        return '<ratingid %r>' % self.ratingid