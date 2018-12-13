from app import db
from app import app



class Newbook(db.Model):
	
    __tablename__ = "Newbooks"
    id = db.Column(db.Integer, primary_key =True)
    book = db.Column(db.String(200))
    author = db.Column(db.String(200))
    genre = db.Column(db.String(200))


        #def __init__(self,book,author,genre):
		#self.book = book
		#self.author = author
		#self.genre = genre

        #def __repr__(self):
		#return '<Book %r>' % self.book
    def __init__(self,book,author,genre):
        self.book = book
        self.author = author
        self.genre = genre

    def __repr__(self):
        return '<Book %r>' % self.book
