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
  def save_account(self):
        '''
        test_save_account test case to test if the crential object is saved into
         the credentials list
        '''
        self.new_credential.save_account()  # saving the new credential
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []
    def test_save_multiple_accounts(self):
            '''
            test_save_multiple_accounts to check if we can save multiple credential
            objects to our Credentials_list
            '''
            self.new_credential.save_account()
            test_credential = Credentials(
                "Linkedin", "", "britney3755")  # new credential
            test_credential.save_account()
            self.assertEqual(len(Credentials.credentials_list), 2)   
    def test_delete_account(self):
                '''
            test_delete_account to test if we can remove a credential from our Credentials list
            '''
            self.new_credential.save_account()
            test_credential = Credentials("Linkedin", "Rita mwaura", "britney3755")  # new credential
            test_credential.save_account()
            self.new_credential.delete_account()  # Deleting a credential object
            self.assertEqual(len(Credentials.credentials_list), 1)  
    def test_search_credential(self):
                '''
            test to check if we can find a credential by account_name and display credentials information
            '''

            self.new_credential.save_account()
            test_credential = Credentials(
                "Linkedin", "Rita mwaura", "britney3755")  # new credential
            test_credential.save_account()

            found_credential = Credentials.search_credential("Linkedin")

            self.assertEqual(found_credential.account_name,
                             test_credential.account_name) 
    def test_credential_exist(self):
            '''
            test to check if we can return a Boolean  if we cannot find the credential.
            '''
            self.new_credential.save_account()
            test_credential = Credentials(
                "Linkedin", "Rita mwaura", "britney3755")  # new credential
            test_credential.save_account()

            credential_exists = Credentials.credential_exist("Linkedin")

            self.assertTrue(credential_exists) 
    def test_display_credentials(self):
            '''
        Test to confrim that we can actually display credential(s) from credentials_list
        that the user has and all the information.i.e account name username(S) and password(s)
        '''
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)   
    def test_copy_password(self):
            '''
        Test to confirm that we can copy the password from a found credential
        so that we can paste it upon login into the respective account.
        '''
        self.new_credential.save_account()
        Credentials.copy_password("Linkedin")
        self.assertEqual(self.new_credential.password, pyperclip.paste())
                   