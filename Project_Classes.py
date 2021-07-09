from Project_Functions import user_menu, enter_website, admin_menu, print_sites, save, load, show_redirection
import json
import os
import time


class Menu:
    def __init__(self):
        self.options = ['1', '2', '3', '4', '5', '6']
        self.filename = "file.json"  # The name of the file that loads & saves all the websites
        self.websites = load(self.filename)  # ^^^^
        if not self.websites:
            self.websites = {"https://platform.itsafe.co.il/": "description 1",
                             "https://www.fxp.co.il/": "description 2",
                             "https://www.google.com/": " description 3"}

    def make_decision(self):  # Options for Main Menu
        while True:
            user_menu()  # User Menu
            decision = input(">>> Pick an option: >")
            if decision not in self.options:
                print("This is not an option.")
            elif decision == "1":
                enter_website()   # -    # SEE IN PROJECT_FUNCTIONS
            elif decision == "3":
                url = input("Enter a valid URL of a website to the list: >>>\n")
                if "http" in url:
                    self.websites[url] = "No description"
                    save(self.websites, self.filename)
                else:
                    print("Invalid URL")

            elif decision == "2":  # Shows a dictionary of all websites within it, appended too.
                print_sites(self.websites)
                input("Press the enter key to continue")

            elif decision == "4":  # Admin MENU
                adm = AdminOptions()
                adm.options()
                self.websites = load(self.filename)
            elif decision == "5":  # Exiting the program
                print("The program will exit in 3 seconds")
                time.sleep(3)
                break


class AdminOptions:  # Admin MENU
    def __init__(self):
        self.decisions = ['1', '2', '3', '4', '5', '6']
        self.filename = "file.json"
        self.password = "admin"  # Password to access the A-MENU

    def options(self):  # OPTIONS for Admin Menu
        counter = 0
        password = input("Enter password: >")
        while password != self.password:
            counter += 1
            password = input(f"Incorrect password, {3 - counter} more tries left: >")
            if counter >= 2:
                print("No more tries left, \nYou are being returned to the Main menu")
                break
        else:
            print("Access Granted! \nYou are now being redirected the Admin Menu.")
            time.sleep(1)
            while True:
                try:
                    admin_menu()
                    choice = str(input(">>> Pick an option: >"))
                    if choice not in self.decisions:
                        print("That is not an option.")
                        continue
                    if choice == "1":  # Loads websites after USER modifications and prints
                        websites = load(self.filename)
                        print_sites(websites)

                        input("Press the enter key to continue")
                    elif choice == "2":  # REMOVE URL from the dictionary as an ADMIN
                        websites = load(self.filename)
                        print_sites(websites)
                        url = input("Enter website to remove, (Remember to delete with website URL): >")
                        if url not in websites:
                            print("Invalid website")
                            continue
                        websites.pop(url)
                        save(websites, self.filename)

                    elif choice == "3":  # edit/remove/add description
                        websites = load(self.filename)
                        print_sites(websites)
                        url = input("Enter website to edit, (Remember to delete with website URL): >")
                        if url not in websites:
                            print("Invalid website")
                            continue
                        desc = input("Enter new description, (Remember to delete with website URL): >")
                        websites[url] = desc
                        save(websites, self.filename)

                    elif choice == "4":
                        break
                except Exception as e:
                    print(e)


menu = Menu()
menu.make_decision()
