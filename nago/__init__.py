from flask import Flask, render_template
from nago.admin.controllers import admin
from nago.main.controllers import main
from nago.admin.UserContorller import manageUser

app = Flask(__name__)

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(manageUser, url_prefix='/admin/user')
app.register_blueprint(main, url_prefix='')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('/404.html')