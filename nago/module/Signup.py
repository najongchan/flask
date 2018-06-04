import re

class Signup:
    # def __init__(self):


    def checkValidate(self, form):
        name = form['name']
        email = form['email']
        username = form['username']
        password = form['password']
        confirm = form['confirm']

        if(self.checkName(name) & self.checkEmail(email) & self.checkUsername(username) & self.checkPassword(password, confirm)):
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

    def checkUsername(self, username):
        if len(username) >= 20:
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
