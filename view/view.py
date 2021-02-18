"""User interface considerations only. Will pass all database queries to the ViewModel """

from .view_util import header, validate_email
import email_validation

class View:

    def __init__(self, view_model):
        self.view_model = view_model

    def get_new_artist(self):

        header('Insert new artist into the database')

        while True:
            artist = self.get_one_new_artist()
            if not artist:
                break

    def get_one_new_artist(self):
        name = input('Enter new artist name to insert, or enter to quit: ')
        if not name:
            return

        email = validate_email(input(f'Input the email address for {name}: '))
            
