#!/usr/bin/env python3.6


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
    print(credentials)

    credentials.save_credentials()


def delete_credentials(credentials):
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
    print("  ✋ Hello, Welcome to Token Box. What is your name?")
    username = input()
    print(f"  Hello {username} 🙂. What would you like to do?")

    while True:
        print(" *" * 21)
        print("  Use these short codes:")
        print(" -" * 12)
        print("🔹 cc -> create credentials\n"
              "🔹 dc -> display credentials\n"
              "🔹 fc -> find credentials\n"
              "🔹 ex -> exit the credentials list")
        print(" *" * 21)
        short_code = input().lower()

        if short_code == 'cc':
            print("New Credential")
            print("-"*10)

            print("Website URL . . . . ")
            web_url = input()

            print("User name . . . . ")
            nick_name = input()

            print("Your password . . . . ")
            pass_code = input()

            save_credentials(create_credentials(web_url, nick_name, pass_code))

            print('\n')
            print(f"👍👍👍👍👍👍😃👍👍👍👍 New token {web_url} {nick_name} created")
            print('\n')

        elif short_code == 'dc':
            if display_credentials():
                print("Here is a list of all your tokens")
                print('\n')

                for credential in display_credentials():
                    print(f"{credential.website} ..... {credential.user_name}")
                print('\n')
            else:
                print('\n')
                print("😞 You don't seem to have any tokens saved yet")
                print('\n')

        elif short_code == 'fc':
            print("Enter the website you want to search for")
            search_url = input()

            if check_existing_credentials(search_url):
                search_credentials = find_credentials(search_url)
                print(f"{search_credentials.website} {search_credentials.user_name}")
                print('-'*20)
                print(f"Website . . . . . {search_credentials.website}")
                print(f"Password: . . . . . {search_credentials.password}")
            else:
                print("🙃 The credential does not exist")

        elif short_code == "ex":
            print("  \n 👋Bye . . . . . . ")
            break

        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
