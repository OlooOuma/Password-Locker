import random
class User :
    '''
    Class that genarates new instances of a User
    '''
    user_list = []
    def __init__(self,username,account,password):
        self.username = username
        self.account = account
        self.password = password

    def save_user(self):
        '''
        save_user method saves usernames into the user list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user method deletes the user info from user_list
        '''
        User.user_list.delete(self)
    @classmethod
    def find_by_account(cls,accoount):
        '''
        Method takes inaccount name and ddisplaysuser info for taht particular account
        Args:
        Account name to search for 
        Returns:
        User info for that account
        '''
        for info in cls.user_list:
            if info.account == account:
                return info

    @classmethod
    def user_exists(cls,account):
        '''
        Method checks if user existsfrom the user_list
        Args:
        account: Account to search if user exists from user_list
        Return:
        Boolean:True or false depending if the user e
    