from flask import Flask, render_template, request, redirect, url_for, jsonify
from forms import Login, Register, AddBooks
from sqlalchemy import and_
from models import Users, Books
from app import app, db









# Test to confirm link of Static and Template -SUCCESS
# Test to test loggin in and homepage features -SUCCESS
# Test to test showing popular books  -SUCCESS
# Testing Registered to User Profile  -
@app.route("/test", methods=['GET', 'POST'])
def test():
    showbooks = Books.query.all()
    print(len(showbooks))
    return render_template('Homepage.html', showbooks = showbooks)



@app.route('/', methods=["GET"])
def home():
    showbooks = Books.query.all()
    print(len(showbooks))
    return render_template('Homepage.html', showbooks = showbooks)

@app.route('/register', methods=['POST','GET'])
def register():
	
	if request.method == "POST":
			username = request.form['username']
			name = request.form['name']
			email = request.form['email']
			password = request.form['pass']
			# Missing to forms
			# birth = request.form['birthday']
			# gender = request.form['gender']
			# phone = request.form['phone']
			# -----
			location = request.form['location']
			age = request.form['age']


			registerform = Users(
								username = username,
								name = name,
								password = password,
								email = email,
								location=location,
								age = age,

								# REMOVED FOR SIMPLIFICATION
								# birth = birth,
								# gender = gender,
								# phone = phone,

								 )
			db.session.add(registerform)
			db.session.commit()
			result = "Success! You can login now!"
			return render_template("register_success.html", result=result)

	return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        usern =  request.form['username']
        passw = request.form['your_pass']
        if Users.query.filter_by(username= usern) and Users.query.filter_by(password = passw):
            print ('You have been logged in!')
            url = '/profile/' + str(usern)
            return redirect(url)
        else:
            result = "invalid"
            return render_template('sign_in.html', form = form, result=result)
    return render_template('sign_in.html')




@app.route('/profile/<usern>', methods=["GET"])
def profile(usern):

    showbooks = Books.query.all()
    print(len(showbooks))

    details = Users.query.filter_by(username= usern).first()
    print(details)



    return render_template('user_profile.html', details=details, showbooks = showbooks)


# TO DO -- Sessionizing Logout and Login so that this would work
@app.route('/logout', methods=["GET", "POST"])
def logout():
    result = 'Logged out!'
    return render_template('logout.html', result = result)


@app.route('/api/search/<keyword>', methods=["GET"])
def search(keyword):
    
    showbooks = Books.query.filter(Books.booktitle.ilike( "%" + keyword + "%" )).all()
    print(showbooks)
    books = []
    for n in showbooks:
        books.append( {"ISBN" : n.isbn, "booktitle" : n.booktitle, "bookauthor" : n.bookauthor,
            "yrpublished" : n.yrpublished, "publisher" : n.publisher, "imgurl1" : n.imgurl1,
            "imgurl2" : n.imgurl2, "imgurl3" : n.imgurl3})
    return jsonify({"status" : 200, "books" : books})

@app.route('/api/book/<booktitle>', methods=["GET"])
def bookdetailsapi(booktitle):

        
    showbooks = Books.query.filter_by(isbn = booktitle).all()
    
    books = []
    for n in showbooks:
        books.append( {"ISBN" : n.isbn, "booktitle" : n.booktitle, "bookauthor" : n.bookauthor,
            "yrpublished" : n.yrpublished, "publisher" : n.publisher, "imgurl1" : n.imgurl1,
            "imgurl2" : n.imgurl2, "imgurl3" : n.imgurl3})
    
    
    return jsonify({"status" : 200, "books" : books})

@app.route('/api/ratings/book/<booktitle>/<userid>', methods=["GET", "POST"])
def bookratingssapi(booktitle, userid):
    
    if request.method ==  "POST":
        dataf = request.args
        ratingform = Rating(bookid = booktitle, userid = userid,
            stars = dataf["stars"], comment = dataf["comment"])
        
        
        db.session.add(ratingform)
        db.session.commit()
        
        return jsonify({"status" : 200})
    else:
        show = Rating.query.filter_by(bookid = booktitle).all()
    
        ratings = []
        for n in show:
            ratings.append( {"ratingid" : n.ratingid, "bookid" : n.bookid, "userid" : n.userid,
                "stars" : n.stars, "comment" : n.comment, "datepublished" : n.datepublished})
        
        return jsonify({"status" : 200, "ratings" : ratings})
        

@app.route('/book/<booktitle>', methods=["GET"])
def bookdetails(booktitle):

        
    showbooks = Books.query.filter_by(isbn = booktitle).all()
    books = []
    for n in showbooks:
        books.append( {"ISBN" : n.isbn, "booktitle" : n.booktitle})
    
    

    return render_template('book_details.html', book = books)



