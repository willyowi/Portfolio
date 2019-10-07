import unittest # Importing the unittest module
from credentials import Credentials # Importing the user class

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials('instagram','kimonyoski','something') #create a new credential object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account,'instagram')
        self.assertEqual(self.new_credentials.u_name,'kimonyoski')
        self.assertEqual(self.new_credentials.p_word,'something')

    def test_save_acc(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_credentials.save_acc() #saving the new user
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_acc(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_credentials.save_acc()
        test_credentials = Credentials('Youtube','peter','drury')
        test_credentials.save_acc()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_acc(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''

        self.new_credentials.save_acc()
        test_credentials = Credentials('Twitter', 'mark','solsjaker')
        test_credentials.save_acc()
        self.new_credentials.delete_acc()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_acc(self):
        '''
        test to check if we can find a user by id number and display information
        '''
        self.new_credentials.save_acc()
        test_credentials = Credentials('4chan','berge','stahl')
        test_credentials.save_acc()
        found_acc = Credentials.find_acc('4chan')
        self.assertEqual(found_acc.account,test_credentials.account)

    def test_credential_exists(self):
        '''
        return bool
        '''
        self.new_credentials.save_acc()
        test_credentials = Credentials('4chan','berge','stahl')
        test_credentials.save_acc()
        credential_exits = Credentials.credential_exists('4chan')
        self.assertTrue(credential_exits)

    def test_display_all_accounts(self):
        self.assertEqual(Credentials.display_acc(),Credentials.credentials_list) # user_name = user
            # p
if __name__ == '__main__':
    unittest.main()
