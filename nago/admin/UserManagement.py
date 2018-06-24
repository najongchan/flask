from nago.module.DB import db

class UserManagement:

    def getUserList(self):
        adminDB = db()
        return adminDB.findMember()