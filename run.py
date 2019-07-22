#!/usr/bin/env python3.6

import random, string

from credentials import Credentials


def create_credentials(web_url, nick_name, pass_code):
    """
    Function to create new credentials
    :param web_url:
    :param nick_name:
    :param pass_code:
    """
    new_credentials = Credentials(web_url, nick_name, pass_code)
    return new_credentials


def save_credentials(credentials):
    """
    Function to save credentials
    :param credentials:
    """
    credentials.save_credentials()


def del_credentials(credentials):
    """
    Function to delete credentials
    :param credentials:
    """
    credentials.delete_credentials()


def find_credentials(website_url):
    """
    Function that finds credentials by website and returns the credntials
    :param website_url:
    """
    return Credentials.find_by_website(website_url)


def check_existing_credentials(website_url):
    """
    Function that checks if credentials exist with that website url and returns a boolean
    :param website_url:
    :return: Boolean
    """
    return Credentials.credential_exists(website_url)


def display_credentials():
    """
    Function that returns all the saved credentials
    """
    return Credentials.display_credentials()


def copy_password(website_url):
    """
    Function that copies the password of the found website url
    :param website_url:
    """
    return Credentials.copy_password(website_url)


def main():
    print("  ✋ Hello, Welcome to TOKEN BOX. What is your name?")
    username = input()
    print("\n")
    print(f"       Hello {username} 🙂")

    while True:
        print(" *" * 15)
        print("  Use these short codes:")
        print(" -" * 12)
        print("🔹 n -> create new token\n"
              "🔹 v -> view saved tokens\n"
              "🔹 f -> find a token\n"
              "🔹 d -> delete a saved token\n"
              "🔹 x -> exit Token Box")
        print(" *" * 15)
        print(" What would you like to do?")
        short_code = input().lower().strip()

        if short_code == 'n':
            print("\n")
            print("   Add New Token")
            print(" -" * 10)

            print(" Input website URL . . . . ")
            web_url = input()

            print(" Input username . . . . ")
            nick_name = input()

            print("\n Type password or use generated password? ")
            print(" -" * 25)
            print(" t -> type password \n g -> generate password")
            print(" -" * 25)
            res = input()
            if res == "t":
                pass_code = input()
            else:
                print("Enter password length: \n")
                try:
                    password_length = int(input().strip())
                except ValueError:
                    print(" Not a number input, will generate a password with length of 8 characters")
                    password_length = 8
                characters = string.ascii_letters + string.punctuation + string.digits
                pass_code = "".join(random.sample(characters, password_length))

            save_credentials(create_credentials(web_url, nick_name, pass_code))

            print(f"\n 👏 New token created"
                  f"\n    Website: {web_url}\n    Username: {nick_name}\n    Password: {pass_code}\n")

        elif short_code == 'v':
            if display_credentials():
                print("Here is a list of all your tokens\n")

                for credential in display_credentials():
                    print("Website ..........Username")
                    print(f"{credential.website} ..... {credential.user_name}")
                print('\n')
            else:
                print("\n😞 You don't seem to have any tokens saved yet\n")

        elif short_code == 'f':
            print("Enter the website you want to search for")
            search_url = input()

            if check_existing_credentials(search_url):
                search_credentials = find_credentials(search_url)
                print(
                    f"{search_credentials.website} {search_credentials.user_name}"
                )
                print('-' * 20)
                print(f"Website . . . . . {search_credentials.website}")
                print(f"Password: . . . . . {search_credentials.password}")
            else:
                print(
                    "\n🙃 The token for that website is not yet added to your Token Box."
                    "\n Type n to create a new token\n")

        elif short_code == "d":
            print("\nEnter website URL for token to be deleted\n")
            delete_url = input()

            if check_existing_credentials(delete_url):
                search_token = find_credentials(delete_url)
                # from credentials import Credentials
                del_credentials(search_token)
                print(f"{search_token} Token deleted")
            else:
                print(
                    "\n🙃 The token for that website is not yet added to your Token Box."
                    "\n Type n to create a new token\n")

        elif short_code == "x":
            print("  \n 👋Bye . . . . . . \n")
            break

        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
