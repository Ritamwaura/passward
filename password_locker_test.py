import unittest  # Importing the unittest module
import pyperclip  # Importing the pyperclip module
from password_locker import Users,Credentials  # Importing the Credentials class

class TestUser(unittest.TestCase):
     '''
     Test a class that defines test cases for the user class behavious
     '''
     self.new_user = Users("Rita mwaura","britney3755"
                           