import unittest  
import pyperclip
from user import User 

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("ritamwaura","britney","ritamwaurabritney","rita") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"ritamwaura")
        self.assertEqual(self.new_user.last_name,"britney")
        self.assertEqual(self.new_user.username,"ritamwaurabritney")
        self.assertEqual(self.new_user.password,"rita")
        

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0703276744","test@user.com") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
            
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","rita","test@user.com") 
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)

def test_find_user_by_name(self):

        self.new_user.save_user()
        test_user = User("Test","user","rita","test@user.com") # new user
        test_user.save_user()
        
        found_user = User.find_by_name("rita")

        self.assertEqual(found_user.password,test_user.password)
        

def test_user_exists(self):


        self.new_user.save_user()
        test_user = User("Test","user","rita","test@user.com") 
        test_user.save_user()

        user_exists = User.user_exist("rita")

        self.assertTrue(user_exists)
        

def test_display_all_users(self):

        self.assertEqual(User.display_users(),User.user_list)
        
def test_copy_password(self):

        self.new_user.save_user()
        User.copy_password("rita")

        self.assertEqual(self.new_user.password,pyperclip.paste())
        

if __name__ == '__main__':
    unittest.main()
