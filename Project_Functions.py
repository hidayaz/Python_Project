import requests
import json
import os

redirecting_sites = []


def show_redirection():
    # Simple function that returns sites that have redirected from the check in Main Menu
    # in default I do not have any.
    return redirecting_sites


def save(websites, filename):  # SAVES ALL CHANGES IN FILE.JSON AUTOMATICALLY
    with open(filename, "w") as fd:
        json.dump(websites, fd)


def load(filename):
    try:
        with open(filename, "r") as fd:
            return json.load(fd)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


def user_menu():  # User Menu
    print("""
                  Main Menu
        -------------------------------
                 Available Menu:
        1) Perform a detailed scan on a website
        2) Show a list of websites in Database
        3) Add a website to the list
        4) Admin Menu (PASSWORD REQUIRED!)
        5) Exit
        """)


def admin_menu():  # 4 in MAIN MENU
    print("""
                  Admin Menu
        -------------------------------
            Available Admin Menu:
        1) Open Websites Database
        2) Delete a URL from the Database (Delete with URL)
        3) Add/Delete/Edit description for a website (Modify with website URL)
        4) Return to Main Menu
        """)


def enter_website():  # 1 in MENU
    try:
        website = input("Enter a valid url of a website to scan: >>> (e.g) https://mybb.com/: \n")
        r = requests.get(website)
        print("Status code is: >", r.status_code)
        print("Response time: >", r.elapsed)
        print("Encoding type: >", r.encoding)
        print("Site is redirecting: >", r.is_redirect)
        if not r.is_redirect:
            pass
        else:
            redirecting_sites.append(url)
            print("You have been redirected from: >", url)
            print("List of redirecting URLS: >", redirecting_sites)
    except Exception as e:
        print("You are only allowed to type a valid URL of a website!\n", e)


def get_ids():  # 2 in MENU
    print("------------ START OF WEBSITES ------------: >")
    counter = 1
    for website in websites:
        print("{0} = {1}".format(counter, website))
        counter += 1
    print("------------ END OF WEBSITES ------------: >")


def add_website():  # 3 in MENU
    website = input("Enter a valid website to the list: >>>\n")
    if "http" in website:
        websites.append(website)
    else:
        print("You can only add to the list a valid URL of a website!")


def get_sites():  # NOT USED ANYMORE
    a_file = open("file.json", "r")
    a_json = json.load(a_file)
    counter = 1
    for website in a_json:
        print("{0} = {1}".format(counter, website))
        counter += 1
    a_file.close()


def print_sites(websites):
    print("------------ START OF WEBSITES ------------: >")
    for counter, website in enumerate(websites.items()):
        print(f"{counter + 1} = {website[0]} : {website[1]}")
    print("------------ END OF WEBSITES ------------: >")
