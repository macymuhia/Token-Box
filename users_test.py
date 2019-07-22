import unittest

from users import User


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Mercy", "macy@gmail.com", "pass123")  # create user object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.name, "Mercy")
        self.assertEqual(self.new_user.user_email, "macy@gmail.com")
        self.assertEqual(self.new_user.user_password, "pass123")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the users list
        """
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.users_list), 1)


if __name__ == '__main__':
    unittest.main()