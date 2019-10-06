import pyperclip
import random,string
from passord_lock import User,credentials
def creat_user(user_name,password):
        '''
        Function to add a new user to our users_list
        '''
        new_User=User(user_name,password)
        
        return new_User
def save_New_User(user_name):
    '''    