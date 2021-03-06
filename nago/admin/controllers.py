from flask import Blueprint, render_template, request, session, flash
from nago.module.Admin import Admin
from nago.admin.UserManagement import UserManagement

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    try:
        if session['admin']:
            print(session['adminId'])
            return render_template('/admin/index.html')
    except KeyError:
        return render_template('/admin/adminLogin.html')


@admin.route('/login', methods=['POST'])
def login():
    dict = request.form.to_dict()
    admin = Admin()

    result = admin.login(dict)

    if result:
        print('login success')
        session['admin'] = True
        session['adminId'] = request.form['adminId']
        return render_template('/admin/index.html')
    else:
        print('login fail')
        flash("일치하는 사용자가 없습니다")
        return render_template('/admin/adminLogin.html')


@admin.route('/logout')
def logout():
    session.pop('admin')
    session.pop('adminId')
    # 로그아웃 처리
    return render_template('/admin/adminLogin.html')


@admin.route('/index')
def mainPage():
    return render_template('/admin/index.html')
