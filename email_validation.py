# Validates email addres to ensure it has @ and . characters

def validate_email(email):
    while True: # Loops until the the email is correct.
        if email.find('@') != -1 and email.find('.') != -1: # checks to make sure @ and . are in the email
            if email.find('@') < email.find('.'): # checks to make sure that @ is before . in an email
                return True
            else:
                print('\nThe @ must come before . in the email\n') 
                email = reenter_email(email) 
        else:
            print('\nMissing @ or . in the email\n') 
            email = reenter_email(email)

def reenter_email(email):
    return input(f'Enter the email address and press ENTER: ')

emailTest = ['abdabc.abc', 'abd@abcabc', 'abc.abc@abc', 'abd@abc.abc']

for email in emailTest:
    validate_email(email)   

