import unittest  # import the unittest module
from credentials import Credentials  # importing the credentials class


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credentials = Credentials("blink.com", "macy",
                                           "pass123")  # create contact object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.website, "blink.com")
        self.assertEqual(self.new_credentials.user_name, "macy")
        self.assertEqual(self.new_credentials.password, "pass123")


if __name__ == "__main__":
    unittest.main()
