"""
Model objects, represent entities in the program, and data in the data store. 
"""

class Artist():
    def __init__(self, name, email): # initializes the class instance
        self.name = name
        self.email = email

    def __str__(self): # returns the string representation of a class object that is human-readable
        return f'{self.name}, {self.email}'

    def __repr__(self): # returns a string representation of an object that is machine-readable
        return f'Name: {self.name}, Email: {self.email}'


    def __eq__(self, other): # used to compare two class objects
        return self.name == other.name and self.email == other.email


    def __ne__(self, other): # used to negate two class objects
        return self.name != other.name or self.email != other.email

class Artwork(Artist):
    def __init__ (self, artist, email, name_artwork, price, availablity=True):
        super().__init__(artist, email) # Call to artist __init__ method

        # Set artwork specific field
        self.name_artwork = name_artwork
        self.price = price
        self.availability = availablity

    