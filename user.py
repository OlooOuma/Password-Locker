import random
class User :
    '''
    Class that generates new instances of a User
    '''
    user_list = []
    def __init__(self, username, account,password):
        self.username = username
        self.account = account
        self.password = password

    def save_user(self):
        '''
        save_user method saves user names into the user list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user method deletes the user info from user_list
        '''
        User.user_list.remove(self)
    @classmethod
    def find_by_account(dts,account):
        '''
        Method takes in account name and displays user info for that particular account
        Args:
            Account name to search for
        Returns:
            User info for that account
        '''
        for info in dts.user_list:
            if info.account == aount:
                return info

    @classmethod
    def user_exists(dts,account):
        '''
        Method checks if user exists from the user_list
        Args:
            account : Account to search if user exists from user_list
        Return:
            Boolean: True or false depending if the user exists
        '''

        for user in dts.user_list:
            if user.account == account:
                return True

        return False

    @classmethod
    def display_users(dts):
        '''
        Method that displays all users
        '''
        return dts.user_list


class Credentials:
    '''
    Class credentials to store credentials for the users
    '''
    def __init__(self, account, password):
        self.password = password
        self.account = account

    def generatePassword():
        chars = 'ABCDEFGHIJKKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        new_pass = ''.join(random.sample(chars, 5))
        return new_pass

    def save_password(self):
        '''
        save_user method saves user names into the user list
        '''
        User.user_list.append(self)