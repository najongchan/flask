from nago.module.DB import db
from operator import eq


class Admin:

    def checkValidate(self, form):
        name = form['name']
        adminId = form['employeeNumber']
        password = form['password']
        repeatPassword = form['repeatPassword']

        if (self.checkName(name) & self.checkAdminId(adminId) & self.checkPassword(password, repeatPassword)) :
            return True
        return False

    def checkName(self, name):
        if(len(name) > 20):
            return False
        return True

    def checkAdminId(self, adminId):
        # 아이디 중복체크
        return True

    def checkPassword(self, password, repeatPassword):
        eq(password, repeatPassword)

    # 로그인
    def login(self, admin):
        adminId = admin['adminId']
        password = admin['password']
        adminDB = db()
        checkValidAdmin = adminDB.findAdmin({"adminId": adminId})

        try:
            if checkValidAdmin['password'] == password:
                return True
            else:
                return False
        except:
            return False
