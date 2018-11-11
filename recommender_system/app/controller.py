import models
from flask import Flask, render_template, request, redirect, url_for
from forms import Login, Register, AddBooks
from sqlalchemy import and_
from models import Users, Books
from app import app, db



@app.route('/', methods=["GET"])
def home():
    showbooks = Books.query.all()
    print(len(showbooks))
    return render_template('Homepage.html', showbooks = showbooks)


# Test to confirm link of Static and Template -SUCCESS
# Test to test loggin in and homepage features -SUCCESS
# Test to test showing popular books  -SUCCESS

@app.route("/test", methods=['GET', 'POST'])
def test():
    showbooks = Books.query.all()
    print(len(showbooks))
    return render_template('Homepage.html', showbooks = showbooks)



@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        usern =  request.form['username']
        passw = request.form['your_pass']
        if Users.query.filter_by(username= usern) and Users.query.filter_by(password = passw):
            print 'You have been logged in!'
            return redirect( url_for('viewbooks'))
        else:
            result = "invalid"
            return render_template('sign_in.html', form = form, result=result)
    return render_template('sign_in.html')



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

@app.route('/sell', methods=['POST','GET'])
def addbooks():
	form = AddBooks()
	if request.method == "POST":
		if form.validate_on_submit():
			isbn = form.isbn.data
			booktitle = form.booktitle.data
			bookauthor = form.bookauthor.data
			yrpublished= form.yrpublished.data
			publisher= form.publisher.data
			imgurl1 = form.imgurl1.data
			imgurl2 = form.imgurl2.data
			imgurl3 = form.imgurl3.data

			addbookForm = Books(isbn = isbn,
								booktitle= booktitle,
								bookauthor = bookauthor,
								yrpublished= yrpublished,
								publisher = publisher,
								imgurl1 = imgurl1,
								imgurl2 = imgurl2,
								imgurl3 = imgurl3
								)
			db.session.add(addbookForm)
			db.session.commit()
			result = "Success! Book added! Please wait for a notification as we suggest a price for your book!"
			return render_template("addbooks.html", form =form, result= result)
	return render_template("addbooks.html", form =form)

@app.route('/bookshelf', methods=['POST','GET'])
def viewbooks():
	showbooks = Books.query.all()
	print(len(showbooks))
	return render_template('index.html', showbooks = showbooks)




@app.route('/console', methods=['POST','GET'])
def admin():
	return render_template('admin.html')