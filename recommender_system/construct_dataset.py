from sqlalchemy import and_
import db

class BooksRatings(db.Model):
	__tablename__ = "BooksRatings"
	id = db.Column(db.String(255), primary_key = True)
	userid = db.Column(db.String(255))
	book = db.Column(db.String(255))
	bookrating= db.Column(db.String(255))



	def __init__(self,userid,book,bookrating):

		self.userid = userid
		self.book = book
		self.bookrating = bookrating


def get_user_id():
    details = BooksRatings.query.with_entities(BooksRatings.userid).all()
    print str(details)




def test_add():

	form = BooksRatings(
						userid = "276726",
						book = "0155061224",
						bookrating = "5",
						 )
	db.session.add(form)

test_add()