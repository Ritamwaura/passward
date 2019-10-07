import pyperclip,random,string
class Users:
    
    users_list=[] # created an empty users list where users will be appended
  def __init__(self,u_Name, pswd):
        '''
        Created an instance of a user 
        '''
        self.u_Name = u_Name
        self.pswd = pswd