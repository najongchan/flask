from flask import Blueprint, render_template, request, session
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

@board.route('/writeView/<id>')
def boardWriteView(id):
    print(id)
    return render_template('/main/board/write.html', writer=id)

# @board.route('/write', method=['POST'])
# def boardWrite:
#
