import unittest  # Importing the unittest module
import pyperclip  # Importing the pyperclip module
from password_locker import Users,Credentials  # Importing the Credentials class

class TestUser(unittest.TestCase):
     '''
     Test a class that defines test cases for the user class behavious
     '''
     self.new_user = Users("Rita mwaura","britney3755"
                           self.new_user = Users("Rita mwaura", "britney3755")  # create user object

    def test_init(self):
        self.assertEqual(self.new_user.u_Name, "Rita mwaura")
        self.assertEqual(self.new_user.pswd, "britney3755")

                           