from app import db
from app import app
from flask_login import UserMixin





        
class Users(db.Model, UserMixin):
	__tablename__ = "Users"
	id= db.Column(db.Integer, primary_key =True)
	name = db.Column(db.String(255))
	username = db.Column(db.String(80), unique = True)
	email = db.Column(db.String(120), unique =True)
	password = db.Column(db.String(255))
	location = db.Column(db.String(255))
	age = db.Column(db.Integer)
	shelfid = db.Column(db.String(36))
	img = db.Column(db.String(255))
	def __init__(self,username,email,password,name, location,age, shelfid, img, active=True):
		self.username = username
		self.email = email
		self.password = password
		self.name=name
		self.location = location
		self.age = age
		self.active = active
		self.shelfid = shelfid
		self.img = img

	def __repr__(self):
		return '<User %r>' % self.username


	# Required for administrative interface
	def __unicode__(self):
		return self.username

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


	def __init__(self,isbn,bookauthor,booktitle,yrpublished,publisher,imgurl1):
		self.isbn = isbn
		self.booktitle = booktitle
		self.bookauthor = bookauthor
		self.yrpublished =yrpublished
		self.publisher = publisher
		# self.imgurl3 = imgurl3
		# self.imgurl2 = imgurl2
		self.imgurl1 =  imgurl1

	def __repr__(self):
		return '<ISBN %r>' % self.isbn




class BooksRatings(db.Model):
	__tablename__ = "BooksRatings"
	id = db.Column(db.Integer, primary_key = True)
	userid = db.Column(db.Integer)
	book = db.Column(db.String(255))
	bookrating= db.Column(db.Integer)



	def __init__(self,userid,book,bookrating):

		self.userid = userid
		self.book = book
		self.bookrating = bookrating

	def __repr__(self):
		return '<ID %r>' % self.userid
