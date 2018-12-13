from app import app, db
from .forms import NewBooks
from flask import Flask, render_template, request, redirect, url_for
from app import models
from .models import Newbook

#init_db()

@app.route('/')
def runit():
    return render_template('index.html')



@app.route('/new_book', methods=['POST', 'GET'])
def new_book():
    
    if request.method == "POST":
    	    book = request.form['book']
    	    author = request.form['author']
    	    genre = request.form['genre']

    	    newbookform = Newbooks(
                                  book = book,
                                  author = author,
                                  genre = genre
    	    	                  )

    	    db.session.add(newbookform)
    	    db.session.commit()
    	    result = "A book has been recommended. Thank you for recommending."
    	    return render_template("recommendedbook.html", result)

    return render_template('index.html')



@app.route('/suggest_book', methods=['POST', 'GET'])
def suggest_book():
	return render_template("new_book.html")
 
