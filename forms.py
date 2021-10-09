from os import name
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import TextAreaField

class TodoForm(FlaskForm):
    title = StringField('Tytuł')
    description = TextAreaField('Opis')
    done = BooleanField('Czy zrobione?')
