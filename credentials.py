class Credentials:
    """
    Class that generates new instances of passwords
    """

    credentials_list = []

    def __init__(self, website, user_name, password):
        """
        __init__ method that helps us define properties for our objects.
        Args:
        website: Website whose credentials need to be saved
        user_name: username of the account
        password: password of the account
        """
        self.website = website
        self.user_name = user_name
        self.password = password


class User:
    """
    Class that generates new instances of a user
    """

    pass
