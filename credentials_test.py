import unittest  # import the unittest module
import pyperclip
from credentials import Credentials  # importing the credentials class


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credentials = Credentials("blink.com", "macy",
                                           "pass123")  # create credentials object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.website, "blink.com")
        self.assertEqual(self.new_credentials.user_name, "macy")
        self.assertEqual(self.new_credentials.password, "pass123")

    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saved into
         the credentials list
        """
        self.new_credentials.save_credentials()  # saving the new credential
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """
        test to check if we can save multiple objects in the credentials list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("example.com", "example", "example123")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        """
        test_delete_credentials to test if we can remove a credential from our credentials list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("example.com", "example", "example123")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials(
        )  # deleting a credentials object
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials_by_website(self):
        """
        test to check if we can find credentials by the website they are created for
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("example.com", "example", "example123")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_website("example.com")
        self.assertEqual(found_credentials.user_name,
                         test_credentials.user_name)

    def test_credentials_exist(self):
        """
        test to check if we can return a Boolean if we cannot find the credentials
        :return: Boolean
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("example.com", "example", "example123")
        test_credentials.save_credentials()

        credentials_exist = Credentials.credential_exists("example.com")
        self.assertTrue(credentials_exist)

    def test_display_all_credentials(self):
        """
        method that returns a list of all credentials saved
        """
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)

    def test_copy_password(self):
        """
        Test to confirm that we're copying the password from found credential
        """
        self.new_credentials.save_credentials()
        Credentials.copy_password("blink.com")

        self.assertEqual(self.new_credentials.password, pyperclip.paste())

    def tearDown(self):
        """
        method to clear instances created during testing when each test runs
        """
        Credentials.credentials_list = []


if __name__ == "__main__":
    unittest.main()
