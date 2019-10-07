import string
import pyperclip
from random import choice


class Credentials:
    credential_list = []


def __init__(self, account, password, account_password):

    self.account = account
    self.password = account_password
    self.account_password = account_password


def save_credential(self):
    '''
    save_credential method saves credentials objects into credential_list
    '''

    Credentials.credential_list.append(self)
    '''
    save_credential method saves credentials objects into credential_list
    '''

@classmethod
def generate_password(cls):
    '''
    Method that generates a random alphanumeric password
    '''

    size = 9

    alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

    password = ''.join(choice(alphanum) for num in range(size))

    return password
