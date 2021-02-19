# deal with view and repository

class ViewModel:

    def __init__(self, db):
        self.db = db

    def insert(self, artist):
        self.db.insert(artist)

    def get_all(self):
        return self.db.get_all()