from flask import Flask, render_template
from nago.admin.controllers import admin
from nago.main.controllers import main
from nago.admin.UserContorller import manageUser
from nago.board.BoardController import board

app = Flask(__name__)

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(manageUser, url_prefix='/admin/user')
app.register_blueprint(main, url_prefix='')
app.register_blueprint(board, url_prefix='/board')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('/404.html')