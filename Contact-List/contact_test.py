
######TEST-ONE ###creating contacts
import unittest # Importing the unittest module
from contact import Contact # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_contact = Contact("James","Muriuki","0712345678","james@ms.com") # create contact object


    def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''

            self.assertEqual(self.new_contact.first_name,"James")
            self.assertEqual(self.new_contact.last_name,"Muriuki")
            self.assertEqual(self.new_contact.phone_number,"0712345678")
            self.assertEqual(self.new_contact.email,"james@ms.com")
# ############TEST-TWO#######saving contacts
    def test_save_contacts(self):
            '''
            test_save_contact test case to test if the contact object is saved into
            the contact list
            '''
            self.new_contact.save_contact() # saving the new contact
            self.assertEqual(len(Contact.contact_list),1)

######TEST-THREE####SAVING MULTIPLE###
    def test_save_multiple_contact(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0702966556","tets@guswer.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)
##########
     def tearDown(self):
         '''
         tearDown method that does clean up test case has run.
         '''
         Contact.contact_list =[]

     def test_save_multiple_contact(self):
         '''
         test_save_multiple contact
         '''
         self.new_contact.save_contact()
         test_contact= Contact ("Test","user","0702966556","tets@user.com")
         test_contact.save_contact()
         self.asserEqual(len(Contact.contact_list),2)

if __name__ == '__main__':
    unittest.main()
