class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] #Empty user list
    def __init__(self,id_number, user_name, password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
        id_number: New user id_number.
        user_name : New user username.
        password: New user password.
        '''

        self.id_number = id_number
        self.user_name = user_name
        self.password = password

    def save_user(self):

        '''
        save_user method that saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_user(cls,id_number):
        '''
        Method that takes in an ID number and returns a user that matches that ID number.

        Args:
            number: ID number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for user in cls.user_list:
            if user.id_number == id_number:
                return user

    @classmethod
    def user_exists(cls,id_number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: ID number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''

        for user in cls.user_list:
            if user.id_number == id_number:
                return True
        return False


    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''

        return cls.user_list
    @classmethod
    def auth_user(cls,user_name,password):
        '''
        method that authenticates user
        '''

        for user in cls.user_list:
            if user.user_name == user_name and user.password == password:
                return True
        return False
