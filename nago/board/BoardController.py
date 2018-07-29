from flask import Blueprint, render_template, request, session, redirect, url_for
from nago.module.Board import Board


board = Blueprint('board', __name__)


@board.route('/')
def boardListView():
    board = Board()
    result = board.viewBoardList()
    boardList = []
    for doc in result:
        boardList.append(doc)

    return render_template('/main/board/list.html', boardList=boardList)

@board.route('/view/<sno>')
def boardView(sno):
    board = Board()
    data = board.viewBoardContent(sno)
    return render_template('/main/board/view.html', data=data)

@board.route('/writeView/<id>')
def boardWriteView(id):
    print(id)
    return render_template('/main/board/write.html', writer=id)


@board.route('/write', methods=['POST'])
def boardWrite():
    data = request.form.to_dict()
    print(data)

    board = Board()
    board.writeBoard(data)

    return '/board'
