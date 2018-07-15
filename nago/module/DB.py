from pymongo import MongoClient

class db:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.mongotest

    # db user find
    # @param    dict    condition
    # @return   dict
    def findMember(self, condition):
        userCollection = self.db.user
        results = userCollection.find_one(condition)
        self.client.close()

        return results


    def findAllMember(self):
        userCollection = self.db.user
        results = userCollection.find();
        self.client.close()

        return list(results)


    # db user insert
    # @param    dict    condition
    # @return   void
    def insertMember(self, condition):
        userCollection = self.db.user
        results = userCollection.insert(condition)
        self.client.close()

        # return results'

    # db connection close
    # @return   void
    def dbClose(self):
        self.client.close()


    def findAdmin(self, condition):
        adminCollection = self.db.admin
        results = adminCollection.find_one(condition)
        self.client.close()

        return results
