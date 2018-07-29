from flask import Blueprint, render_template, request, make_response
from nago.module.Admin import Admin
from nago.admin.UserManagement import UserManagement

manageUser = Blueprint('manageUser', __name__)


@manageUser.route('/')
def userListPage():
    userManagement = UserManagement()
    userList = userManagement.getUserList()
    return render_template('/admin/userList.html', userList=userList)


@manageUser.route('/delete', methods=['POST'])
def deleteUser():
    data = request.form['userId']

    userManagement = UserManagement()
    userManagement.deleteUser(data)
    print(data)
    resp = make_response()
    resp.status_code = 200
    return resp

# @manageUser.route('/content', methods=['GET'])
# def getUserContent():
#     data = request.form['userId']
#
#     userManagement = UserManagement()
#     userManagement.getUserContent(data)
#
#     print(data)
#     resp = make_response()
#     resp.status_code = 200
#     resp.
