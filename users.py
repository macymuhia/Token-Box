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
