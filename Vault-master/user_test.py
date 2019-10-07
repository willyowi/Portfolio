import unittest # Importing the unittest module
from password import User # Importing the user class
from credentials import Credentials


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('1234','cartelo','kimonyoski') #create a new user object
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.id_number,'1234')
        self.assertEqual(self.new_user.user_name,'cartelo')
        self.assertEqual(self.new_user.password,'kimonyoski')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_user.save_user()
        test_user = User('4567','eugene','kaspersky')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''

        self.new_user.save_user()
        test_user = User('5678','darth','maul')
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_ID(self):
        '''
        test to check if we can find a user by id number and display information
        '''

        self.new_user.save_user()
        test_user = User('0987','darth','vader')
        test_user.save_user()

        found_user = User.find_user('0987')

        self.assertEqual(found_user.id_number,test_user.id_number)

    def test_user_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User('123','marcus','hopsin')
        test_user.save_user()

        user_exists = User.user_exists('123')

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_users(),User.user_list) # user_name = user
            # p

    def test_auth_users(self):
        '''
        checks if username and password matches
        '''

        self.new_user.save_user()
        test_user = User('6561','scooby','doo')
        test_user.save_user()
        auth_users = User.auth_user('scooby','doo')
        self.assertTrue(auth_users)

if __name__== '__main__':
    unittest.main()
