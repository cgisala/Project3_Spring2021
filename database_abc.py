import abc

class ArtistDB(abc.ABC):
    @abc.abstractmethod
    def insert(self, artist):
        pass

class ArtworkDB(abc.ABC):
    @abc.abstractmethod
    def insert(self, artwork):
        pass
    
    @abc.abstractmethod
    def search(self, artist):
        pass
