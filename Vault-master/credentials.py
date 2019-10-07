import secrets

class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = [] #Empty user list

    def __init__(self,account, u_name, p_word):

        self.account = account
        self.u_name = u_name
        self.p_word = p_word

    def save_acc(self):
        '''
        save_acc method that saves account objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_acc(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        Credentials.credentials_list.remove(self)
    @classmethod
    def find_acc(cls,account):
        '''
        Method that takes in an account name and returns an account that matches that name.

        Args:
            name: account name to search for
        Returns :
            account that matches the account name.
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
        return False

    @classmethod
    def credential_exists(cls,account):
        '''
        Method that checks if an account exists from the credentials list.
        Args:
            name: account name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_acc(cls):
        '''
        method that returns the user list
        '''

        return cls.credentials_list

    @classmethod
    def pass_gen(cls):
        '''
        function that generates a random password
        '''
        p_word = secrets.token_urlsafe(8)
        return p_word
