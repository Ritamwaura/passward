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
if short_code == 'ca':
        uName=input("Enter Your prefered username").capitalize()
        pswd = input("Enter Your Password As Well")
        save_New_User(create_user(uName,pswd))
 elif short_code == 'li' :   
        
        user_name=input("Enter UserName").capitalize()
        password=input("Paste Password")
        validate_user=(authenticate_User(user_name,password))
        
    if validate_user == user_name:
            print(f"Hello {user_name}.Welcome To PassWord Locker Manager")  
            print('\n')
            print("what would you like to do?")
            print('\n')
 while True:
             print("Use these short codes : cc - Create a new credential, dc - Display Credential(s), fc - Find a credential,ex - Exit the application, gp- Generate A randomn password, del- Delete credential,cp-Copy Password")
                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print("Account name ....")
                            account_Name = input().capitalize()

                            print("Your Account name ...e.g LinkedIn username")
                            user_Name = input()
                            while True:
                                print(" For Type/Paste Password type TP ; For generate_Password type gp")
                                password_Choice = input("Enter").lower()
                                if password_Choice == 'tp':
                                    user_Password = input("Enter Password")
                                    break
                                elif password_Choice == 'gp':
                                    user_Password = generate_Password()
                                    break
                                elif password_Choice != 'tp' or 'gp':
                                    print("Invalid password please try again")
                                    break
                                else:
                                    print("Invalid password please try again")
                            save_credentials(create_credential(account_Name,user_Name,user_Password))
                            print('\n')
                            print(f"New Credential : {account_Name} UserName: {user_Name}  created")
                            print('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Your Account(s) Credential(S) are as follows :")
                                    print('\n')
                                    for password_locker in display_credentials():
                                            print(f"Account Name :{password_locker.account_name} ; UserName: {password_locker.user_name} ; PassWord :{password_locker.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print(
                                        "Oops !!! You dont seem to have any Credentials saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the Account Name you want to search for")
                            search_name = input().capitalize()
                            if check_existing_credendtials(search_name):
                                    search_credential = find_credential(
                                        search_name)
                                    print(f"Account Name : {search_credential.account_name}")
                                    print('-' * 100)
                                    print(f"Account Name: {search_credential.account_name} PassWord :{search_credential.password}")
                            else:
                                    print("That Credential does not exist")
                                    print('\n')
					
                    elif short_code == 'cp':

                        	print("Enter the account name of the Credentials you want to generate password for")
                        	search_name = input().capitalize()
                        	if check_existing_credendtials(search_name):
                            		search_credential = find_credential(search_name)
                            		print(f"{search_credential.account_name}")
                            		print("_"*20)
                            		user_Password=copy_password(search_name)
                            		print('\n')
                            		print(f"New Credential : {account_Name} UserName: {user_Name}  You can proceed and paste to your account")
                                             
                    elif short_code == "del":
                         print("Enter the account name of the Credentials you want to delete")
                         search_name = input().capitalize()
                         if check_existing_credendtials(search_name):
                             search_credential = find_credential(search_name)
                             print(
                                 f"{search_credential.account_name}")
                             print("_"*20)
                             password_locker.delete_account()
                             print('\n')
                             print(f"New Credential : {account_Name} UserName: {user_Name}  successfully deleted!!!")
                             print('\n')
                         else:
                                    print("That Credential does not exist")
                                     
                    elif short_code == 'gp':
                    		user_Password = generate_Password()
                  
              	
                    elif short_code == 'ex':
                        print("Happy Coding See You Dear")
                        break
                    else:
                        print("Invalid response kindly refer to the Menu above")
           
                


