from flask import Flask, Blueprint, render_template, request
from pymongo import MongoClient
from pprint import pprint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from nago.module.Signup import Signup



# from flask import Flask, render_template, session, redirect, url_for, flash, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('/main/index.html')

@main.route('/signup', methods=['POST'])
def login():
    pprint(request)
    pprint(request.form)
    dict = request.form
    name = dict['name']

    checker = Signup()
    if checker.checkValidate(request.form) == True:
        return render_template('/main/user.html', name = name)
    else:
        return 'Fail'
