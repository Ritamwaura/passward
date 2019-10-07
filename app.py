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

def save_credential(password_locker):
    """
    Function to save credentials
    """
    password_locker.delete_account()
 def find_credential(account_Name):
     """
     function that find credential by account name and return credential
     """        

def copy_password(account_Name):
       """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    Credentials.copy_password(account_Name)
def generate_Password():
        '''
        generates a 9 digit randomn password
        '''
        auto_Generic_Password=Credentials.generate_Password()
        return auto_Generic_Password
def main():
    print("Hello Welcome to your Credentials list.Create An Account : CA or Already Have An Account LI? :")
    short_code=input("CA , LI").lower()


