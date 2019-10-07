import unittest  # Importing the unittest module
import pyperclip  # Importing the pyperclip module
from password_locker import Users,Credentials  # Importing the Credentials class

class TestUser(unittest.TestCase):
    '''Test class that defines test cases for the Users class behavious.
    '''
    def setUp(self):
        '''