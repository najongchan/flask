from nago.module.DB import db


class UserManagement:

    def getUserList(self):
        adminDB = db()
        return adminDB.findAllMember()


    def deleteUser(self, userId):
        adminDB = db()
        return adminDB.deleteMember(userId)

