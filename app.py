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
    This function update our users_list with anew user
    '''
    User.user_list.append(user_name)
def authenticate_user(us_name,pwd):
    '''
    This function  authenticates the current user in our application
    '''
    authenticate_user=credentials.confirm_User(us_name,pwd)
    return authenticate_user
def creat_credential(account_Name,user_name,user_password):
    """
    Function to creat a new Credentials
    """
    new_credential=credentials.(
        account_Name,user_name,user_password)
    return new_credential

    )        
    