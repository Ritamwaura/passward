import pyperclip,random,string
class Users:
    
    users_list=[] # created an empty users list where users will be appended
  def __init__(self,u_Name, pswd):
        '''
        Created an instance of a user 
        '''
        self.u_Name = u_Name
        self.pswd = pswd
  def save_user(self):
            '''
        save_user method saves users in our class Users inside the users_list
        '''
        Users.users_list.append(self)
         
  def save_user(self):
            '''
        save_user method saves users in our class Users inside the users_list
        '''
        Users.users_list.append(self)
  class Credentials:
    
        """
        Class that generates new instances of the credentials for the various accounts.
        """

        credentials_list = []  # Empty credentials list
        @classmethod
        def confirm_User(cls,u_Name, pswd):
            '''Created a function to confirm 
        whether the active user is in our users list or not
        '''
        active_user = ''
        for user in Users.users_list:
            if(user.u_Name == u_Name and user.pswd == pswd):
                    active_user == user.u_Name
        return active_user