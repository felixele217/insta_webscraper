"""
project description: web scraping instagram for followers
author: felixele217
created: november 2020
"""

import re
import string

import requests
from bs4 import BeautifulSoup

BASIC_URL_FORMAT = "https://www.instagram.com/"


print("Hey there, i will tell you the amount of followers for the following Instagram accounts.")
print("Just make sure to type the account name correctly, otherwise I cannot help you! :(")
print("You can press q to quit anytime.")


# this functions gets the html content from an instas user page and parses it with beautifulsoup
# so that it can be accessed easier
def get_content(URL, name):
    try:
        page = requests.get(URL)
        page.encoding = "ISO-885901"
    except requests.exceptions.MissingSchema:
        print("There is no user with the name ", account_name)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup


# this function searches for the followers in the parsed html page and returns its value
# if there is no such an account it returns false
def get_followers(content):
    try:
        desc = content.find("meta", property="og:description")
        s = desc.attrs['content']
        s = s.split("-")[0]
        s = s.split(" ")
        number_of_followers = s[0]
        return number_of_followers
    except AttributeError:
        print("There is no such user!")
        return None


def print_dict(dict):
    for key, value in dict.items():
        print(key," has ", value, " followers.")


names = {}

# this is basically the program code where everything happens
while True:

    account_name = input("Enter the account: ")

    # NOTE: "q" is not a valid Instagram handle because they must be at least 3 characters
    if account_name == "q":
        break
    else:
        URL = BASIC_URL_FORMAT + account_name + "/"
        # getting the html content from the users insta page parsed with BeautifulSoup
        content = get_content(URL, account_name)
        # returning the number_of_followers. if the account does not exist returns False
        number_of_followers = get_followers(content)
        # add the account with its followers to the names dictionary
        names[account_name] = number_of_followers
        if number_of_followers:
            print(account_name, " has ", names[account_name], " followers on Instagram.")


