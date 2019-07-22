import unittest

from users import User


class TestUser(unittest.TestCase):
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
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from our users list
        """
        self.new_user.save_user()
        test_user = User("Aviana", "aviavi", "avi123")
        test_user.save_user()

        self.new_user.delete_user()  # deleting a user object
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        """
        method to clear instances created during testing when each test runs
        """
        User.user_list = []


if __name__ == '__main__':
    unittest.main()