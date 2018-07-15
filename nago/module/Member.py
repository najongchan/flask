import re
from nago.module.DB import db


class Member:
    # def __init__(self):


    def checkValidate(self, form):
        name = form['name']
        email = form['email']
        id = form['id']
        password = form['password']
        confirm = form['confirm']

        if(self.checkName(name) & self.checkEmail(email) & self.checkId(id) & self.checkPassword(password, confirm)):
            return True
        return False


    def checkName(self, name):
        if len(name) >= 20:
            return False
        return True

    def checkEmail(self, email):
        result = re.match('[0-9a-zA-Z][_0-9a-zA-Z-]*@[_0-9a-zA-Z-]+(\.[_0-9a-zA-Z-]+){1,2}$', email)

        if result:
            return True
        else:
            return False

    def checkId(self, id):
        if len(id) >= 20:
            return False
        return True

    def checkPassword(self, password, confirm):
        password = password.strip()
        confirm = confirm.strip()

        result = re.match('^.*(?=.{6,20})(?=.*[0-9])(?=.*[a-zA-Z]).*$', password)

        if (result != None) & (password == confirm):
            return True
        else:
            return False

    # 회원가입
    # @param    dict    memberData  유저 입력 정보
    # @return   void
    def addMember(self, memberData):
        del memberData['confirm']

        memberDB = db()
        memberDB.insertMember(memberData)

        return

    # 로그인
    # @param    dict    memberData  유저 입력 정보
    # @rerutn   bool
    def loginMember(self, memberData):
        id = memberData['id']
        print(type(id))
        pwd = memberData['password']
        print(memberData)
        memberDB = db()
        dbData = memberDB.findMember({"id": id})
        print(dbData)
        if dbData['password'] == pwd:
            return True
        else:
            return False
