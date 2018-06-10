from flask import Blueprint, render_template, request, session
from nago.module.Admin import Admin

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    return render_template('/admin/adminLogin.html')


@admin.route('/login', methods=['POST'])
def login():
    dict = request.form.to_dict()
    admin = Admin()

    result = admin.login(dict)

    if result:
        print('login success')
        session['admin'] = True
        return render_template('/admin/index.html')
    else:
        print('login fail')
        return render_template('/admin/adminLogin.html')


@admin.route('/logout')
def logout():
    session.pop('admin')
    # 로그아웃 처리
    return render_template('/admin/adminLogin.html')
