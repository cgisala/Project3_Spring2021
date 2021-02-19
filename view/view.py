"""User interface considerations only. Will pass all database queries to the ViewModel """

from exceptions.email_error import EmailError
from .view_util import header, validate_email
from model.model import Artist, Artwork

class View:

    def __init__(self, view_model):
        self.view_model = view_model

    def get_new_artist(self):

        header('Insert new artist into the database')

        while True:
            artist = self.get_one_new_artist()
            if not artist:
                break
    
    # Gets artist name and email
    def get_one_new_artist(self):
        name = input('Enter new artist name to insert, or enter to quit: ') # prompts the user to enter the artist name
        if not name:
            return

        # validate email address
        email = validate_email(input(f'Input the email address for {name}: ')) 
        artist = Artist(name, email)
        try:
            self.view_model.insert(artist)
            return artist
        except EmailError as e: # prints email error messages
            print(str(e))

    # To do create get_new_artwork method
    # To do search artwork by an an artist method
    # To do display available artwork by an artist
    # To do add  a new artwork.  ensure the artwork is associated with an artist
    # Delete an artwork
    # change the availability status of an artwork, fro example change from available to sold

            
