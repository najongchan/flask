from pymongo import MongoClient

class db:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/flask')
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

    # db board find title
    # @return   dict
    def findBoardTitle(self):
        boardCollection = self.db.board
        results = boardCollection.find({}, {"title" : 1, "sno" : 1}).limit(10)
        self.client.close()

        return results

    # db board find content
    # @param    dict    condition
    # @return   dict

    def findBoardContent(self, condition):
        boardCollection = self.db.board
        results = boardCollection.find(condition)
        self.client.close()

        return results

    # db board insert
    # @param    dict    condition
    # @return   void
    def insertBoard(self, condition):
        boardCollection = self.db.board
        results = boardCollection.insert(condition)
        self.client.close()


