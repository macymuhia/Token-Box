import pyperclip


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

    def save_credentials(self):
        """
        save_credentials method saves credentials objects into credentials_list
        """

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method deletes a saved contact from the contact list
        :return:
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_website(cls, website_url):
        """
        method that takes in a website and returns credentials that match that website
        Args:
            website_url: website to search for
        Returns:
            credentials that match the website
        """

        for credential in cls.credentials_list:
            if credential.website == website_url:
                return credential

    @classmethod
    def credential_exists(cls, website_url):
        """
        Method checks if a credential exists from the credentials list
        :param website_url: website_url to search if it exists
        :return: Boolean: True or False depending on whether the credential exists
        """
        for credential in cls.credentials_list:
            if credential.website == website_url:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        method that returns the credentials list
        :return: List
        """
        return cls.credentials_list

    @classmethod
    def copy_password(cls, website_url):
        credentials_found = Credentials.find_by_website(website_url)
        pyperclip.copy(credentials_found.password)
