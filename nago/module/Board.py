import regit
from nago.module.DB import db

class Board:
    # def __init__(self):

    # 글작성
    # @param    dict    boardData   게시글 데이터
    # @return   void
    def writeBoard(self, boardData):
        boardDB = db()
        boardDB.insertBoard(boardData)

        return

    # 게시판 리스트 출력
    # @rerutn   dict
    def viewBoardList(self):
        boardDB = db()
        boardList = boardDB.findBoardTitle()

        return boardList

    # 게시글 내용 출력
    # @param    int     sno     게시글 번호
    # @return   dict
    def viewBoardContent(self, sno):
        boardDB = db()
        contents = boardDB.findBoardContent({"sno": sno})

        return contents