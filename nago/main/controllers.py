from flask import Flask, Blueprint, render_template, request, session
from pprint import pprint
from nago.module.Member import Member
from nago.module.Board import Board



# from flask import Flask, render_template, session, redirect, url_for, flash, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('/main/index.html')

@main.route('/signup')
def signupPage():
    return render_template('/main/signup.html')

@main.route('/signup', methods=['POST'])
def signupRoute():
    dict = request.form.to_dict()
    member = Member()
    if member.checkValidate(request.form) == True:
        member.addMember(dict)
        return render_template('/main/index.html')
    else:
        return 'Fail'

@main.route('/login')
def loginPage():
    return render_template('/main/login.html')

@main.route('/login', methods=['POST'])
def loginRoute():
    dict = request.form.to_dict()
    member = Member()
    result = member.loginMember(dict)

    if result == True:
        session['logged_in'] = True
        return render_template('/main/user.html')
    else:
        return render_template('/main/login.html')

@main.route('/board/list')
def boardListView():
    board = Board()
    result = board.viewBoardList()
    boardList = []
    for doc in result:
        boardList.append(doc)

    return render_template('/main/board/list.html', boardList=boardList)