class User:
    """
    Class that generates new instances of a user
    """

    user_list = []

    def __init__(self, name, user_email, user_password):
        """
        __init__ method that helps us define properties for our objects.
        Args:
        name: Website whose credentials need to be saved
        user_email: user email of the account
        user_password: password of the user account
        """
        self.name = name
        self.user_email = user_email
        self.user_password = user_password

    def save_user(self):
        """
        save_user method saves users objects into users_list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes a saved user from the user list
        :return:
        """
        User.user_list.remove(self)

    @classmethod
    def find_by_email(cls, u_name):
        """
        method that takes in a email and returns user that matches that email
        Args:
            u_name: user email to search for
        Returns:
            user that matches the email
        """

        for user in cls.user_list:
            if user.user_email == u_name:
                return user

    @classmethod
    def exists(cls, u_name):
        """
        Method checks if a user exists from the users list
        :param u_name: u_name to search if user exists
        :return: Boolean: True or False depending on whether the user exists
        """
        for user in cls.user_list:
            if user.user_email == u_name:
                return True
        return False

    @classmethod
    def display_users(cls):
        """
        method that returns the users list
        :return: List
        """
        return cls.user_list
