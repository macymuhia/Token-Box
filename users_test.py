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
        test_user = User("Aviana", "avi@gmail.com", "avi123")
        test_user.save_user()

        self.new_user.delete_user()  # deleting a user object
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        """
        test to check if we can save multiple objects in the users list
        """
        self.new_user.save_user()
        test_user = User("Aviana", "avi@gmail.com", "avi123")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_find_credentials_by_email(self):
        """
        test to check if we can find users by their email
        """
        self.new_user.save_user()
        test_user = User("Aviana", "avi@gmail.com", "avi123")
        test_user.save_user()

        found_user = User.find_by_email("avi@gmail.com")
        self.assertEqual(found_user.name, test_user.name)

    def test_user_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the user
        :return: Boolean
        """
        self.new_user.save_user()
        test_user = User("Aviana", "aviavi", "avi123")
        test_user.save_user()

        user_exists = User.exists("aviavi")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(), User.user_list)

    def tearDown(self):
        """
        method to clear instances created during testing when each test runs
        """
        User.user_list = []


if __name__ == '__main__':
    unittest.main()