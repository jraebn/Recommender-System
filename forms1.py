from flask_wtf import Form
from wtforms import StringField, validators, SubmitField
from wtforms.validators import InputRequired, Length

class NewBooks(Form):
    book = StringField('Book',[validators.DataRequired(),validators.Length(min=5, max = 120)])
    author = StringField('Author',[validators.DataRequired(),validators.Length(min=5, max = 120)])
    genre = StringField('Genre',[validators.DataRequired(),validators.Length(min=5, max = 120)])
    submit = SubmitField("New Book")