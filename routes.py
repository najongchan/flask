from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from pprint import pprint


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('register')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])     # 데코레이트 패턴
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/mongo/', methods=['GET','POST'])
def mongoTest():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.mongotest
    collection = db.user
    results = collection.find()
    client.close()
    strgg = ''
    for document in results:
        print(document)
        strgg += 'name : ' + document['name'] + ' / comment : ' + document['comment'] + '\n'

    return strgg
    # return render_template('/mongo.html', data=results, collection=collection.name)

@app.route('/sign_up', methods=['POST'])
def regist():
    pprint(request.form)
    return 1


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# @app.error_handlers(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
#
# @app.error_handlers(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
    # app.run (host='0.0.0.0', port=5000, debug=True)

