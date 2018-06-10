from flask import Blueprint, render_template, request, session
from nago.module.Admin import Admin

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    return render_template('/main/adminLogin.html')


@admin.route('/login', methods=['POST'])
def login():
    dict = request.form.to_dict()
    admin = Admin()

    result = admin.login(dict)

    if result:
        print('login success')
    else:
        print('login fail')


@admin.route('logout')
def logout():
    # 로그아웃 처리
    return True
