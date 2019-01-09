import models
import flask_login
from wtforms import PasswordField
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from forms import Login, Register, AddBooks
from sqlalchemy import and_
from models import Users, Books, BooksRatings
from app import app, db
import time, json
from collaborative_filtering import user_reommendations
from werkzeug.utils import secure_filename



ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


# Test to confirm link of Static and Template -PASS
# Test to test loggin in and homepage features -PASS
# Test to test showing popular books  -PASS
# Testing Registered to User Profile  - PASS
# Testing Make sure that each click goes to specific route -
# @app.route("/test", methods=['GET', 'POST'])
def test():
    details = BooksRatings.query.with_entities(BooksRatings.userid).all()
    list_ = []
    for detail in details:
        detail = str(detail)
        detail = detail.replace(")","")
        detail = detail.replace("(","")
        detail = detail.replace(",","")
        list_.append(int(detail))

    list_user = list(set(list_))

    ds = {}
    for user in list_user:
        data_ =  BooksRatings.query.filter_by(userid = user)

        books_of_user = {}
        for data in data_:
            dict_={str(data.book):int(data.bookrating)}
            books_of_user.update(dict_)
            
        ds.update({str(user):books_of_user})




    recommendations = user_reommendations(ds, "276762")
    print(recommendations)

    # f.write(str(ds))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_recommendations(shelfid):
    details = BooksRatings.query.with_entities(BooksRatings.userid).all()
    list_ = []
    for detail in details:
        detail = str(detail)
        detail = detail.replace(")","")
        detail = detail.replace("(","")
        detail = detail.replace(",","")
        list_.append(int(detail))

    list_user = list(set(list_))

    ds = {}
    for user in list_user:
        data_ =  BooksRatings.query.filter_by(userid = user)

        books_of_user = {}
        for data in data_:
            dict_={str(data.book):int(data.bookrating)}
            books_of_user.update(dict_)
            
        ds.update({str(user):books_of_user})




    recommendations = user_reommendations(ds, shelfid)
    print(recommendations)
    return recommendations

@app.route("/login", methods=['GET', 'POST'])
def login1():


    if request.method == 'POST':
        usern =  request.form['username']
        passw = request.form['your_pass']
        if Users.query.filter_by(username= usern) and Users.query.filter_by(password = passw):
            print 'You have been logged in!'
            url = '/profile/' + str(usern)
            return redirect(url)
        else:
            result = "invalid"
            return render_template('sign_in.html', form = form, result=result)
    return render_template('sign_in.html')



@app.route("/bookui", methods=['GET', 'POST'])
def ui():
    isbn = "0002005018"
    book = Books.query.filter_by(isbn=str(isbn)).first()

    return render_template('book_details.html', book=book)

@app.route('/', methods=["GET"])
def home():
    showbooks = Books.query.all()
    print(len(showbooks))
    return render_template('Homepage.html', showbooks = showbooks)

@app.route('/register', methods=['POST','GET'])
def register():
	
    if request.method == "POST":

            file = request.files['file']
            if 'file' not in request.files:
                print 'No file part'
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
               


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
                shelfid = '276762'
                img = str(file.filename)


                registerform = Users(
                                    username = username,
                                    name = name,
                                    password = password,
                                    email = email,
                                    location=location,
                                    age = age,
                                    shelfid = shelfid,
                                    img = img,


                                    )
                db.session.add(registerform)
                db.session.commit()
                result = "Success! You can login now!"
                return render_template("register_success.html", result=result)

    return render_template("register.html")




@app.route('/profile/<usern>', methods=["GET"])
def profile(usern):

    if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
               
                isbn = request.form['isbn']
                bookauthor = request.form['author']
                booktitle = request.form['title']
                yrpublished = request.form['yrpub']
                publisher = request.form['pub']
                img = str(file.filename)
# 9724119378
# (self,isbn,bookauthor,booktitle,yrpublished,publisher,imgurl1)

                form = Books(
                                    isbn=isbn,
                                    bookauthor = bookauthor,
                                    booktitle = booktitle,
                                    yrpublished = yrpublished,
                                    publisher=publisher,
                                    imgurl1 = img,

                                    )
                db.session.add(form)
                db.session.commit()
                return redirect('/profile/' + str(usern))

    showbooks = Books.query.all()
    print(len(showbooks))

    details = Users.query.filter_by(username= usern).first()
    print(details)
    
    recommended = get_recommendations(details.shelfid)

    print str(details.shelfid) + '<---'



    return render_template('user_profile.html', details=details, recommended = recommended, showbooks = showbooks)



# 0002005018
@app.route('/profile/<usern>/book/<isbn>', methods=["GET", "POST"])
def specific_book(usern, isbn):
    # isbn = "0002005018"

    book = Books.query.filter_by(isbn=str(isbn)).first()
    details = Users.query.filter_by(username= usern).first()
    status = ''
    if request.method == 'POST':

        url = 'http://localhost:5000/profile/' + str(details.username) + '/book/' + str(isbn)
        print str(url)
        option = request.form['rating']
        details = details.shelfid
        book = book.isbn

        print str(details) +','+ str(book)+','+ str(option)

        form = BooksRatings(
                            userid = int(details),
                            book = str(book),
                            bookrating = int(option))
        db.session.add(form)
        db.session.commit()
        status = 'Success'
        book = Books.query.filter_by(isbn=str(isbn)).first()
        details = Users.query.filter_by(username= usern).first()
        return render_template('book_details.html', details = details, book=book, status=status)

    else:
        return render_template('book_details.html', details = details, book=book, status=status)


# TO DO -- Sessionizing Logout and Login so that this would work
@app.route('/logout', methods=["GET", "POST"])
def logout():
    result = 'Logged out!'
    return render_template('logout.html', result = result)



# @app.route('/api/search', methods=["GET"])
# def search():


@app.route('/admin', methods=['POST','GET'])
def admin():
    return render_template('admin.html')



@app.route('/api/search', methods=["GET"])
def search():


    dataf = request.args
    
    
    showbooks = Books.query.filter(Books.booktitle.contains(dataf["keyword"])).all()
    print(len(showbooks))
    books = []
    for n in showbooks:
        books.append( {"ISBN" : n.isbn, "booktitle" : n.booktitle})
    print (books)
    

    return jsonify({"status" : 200, "books" : books})

@app.route('/api/book/<booktitle>', methods=["GET"])
def bookdetailsapi(booktitle):

        
    showbooks = Books.query.filter_by(booktitle = booktitle).all()
    books = []
    for n in showbooks:
        books.append( {"ISBN" : n.isbn, "booktitle" : n.booktitle})
    print (books)
    

    return jsonify({"status" : 200, "books" : books})

@app.route('/book/<isbn>', methods=["GET"])
def bookdetails(isbn):

        
    book = Books.query.filter_by(isbn=str(isbn)).first()

    return render_template('book_details_home.html', book = book)




