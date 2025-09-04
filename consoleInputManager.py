import contactManager

class ConsoleInputManager:
    contactManager = None

    def __init__(self):
        self.contactManager = contactManager.ContactManager()

    def __getContactInfoFromUser(self):
        name = input("Enter name: ")
        email = input("Enter email id: ")
        phone = input("Enter phone no: ")
        return (name, email, phone)

    def __addContactToContacts(self):
        name, email, phone = self.__getContactInfoFromUser()
        self.contactManager.addContact(name, email, phone)
        print ("Successfully added contact!")
        print()

    def __deleteContactFromContacts(self):
        name, email, phone = self.__getContactInfoFromUser()
        self.contactManager.deleteContact(name, email, phone)

    def __createSearch(self):
        done = False
        name = ""
        email = ""
        phone = ""

        while not done:
            print("""What info do you want to search on?
                Name
                Email
                Phone""")
            respond = input()
            if respond.lower() == "name":
                name = input("Enter name to search: ")
            else:
                if respond.lower() == "email":
                    email = input("Enter email to search: ")
                else:
                    if respond.lower() == "phone":
                        phone = input("Enter phone number to search: ")
                    else:
                        print("Please enter a valid input")
            print("Do you want to enter more info? (yes/no)")
            done = input().lower() == "no"
        self.contactManager.searchContacts(name, email, phone)

    def __parse(self, respond):
        if respond.lower() == "list":
            self.contactManager.listContacts()
            return True
        if respond.lower() == "add":
            self.__addContactToContacts()
            return True
        if respond.lower() == "delete":
            self.__deleteContactFromContacts()
            return True
        if respond.lower() == "delete all":
            self.contactManager.deleteAllContacts()
            print("Sucessfully deleted all contacts.")
            print()
            return True
        if respond.lower() == "search":
            self.__createSearch()
            return True
        if respond.lower() == "close":
            print("Thank You!")
            return False
        else:
            print("Please try again!")
            print()
            return True

    def run(self):
        running = True
        intro = "Address Book Project!"
        mainMenu = """What do you want to do? 
        | List       - Lists all saved contacts     |
        | Add        - Adds a contact               |
        | Delete     - Deletes a contact            |
        | Delete all - Removes all contacts         |
        | Search     - Searches for a contact       |
        | Close      - Closes the address book      |      
            (Your entry isn't case sensitive!)"""
        print(intro)
        while running:
            print(mainMenu)
            respond = input()
            running = self.__parse(respond)