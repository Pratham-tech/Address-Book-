class ContactManager:
    __addContactList = []
    
    def addContact(self, name, email, phone):
        self.__addContactList = []
        self.__addContactList.append(Contact(name, email, phone))
        for contact in self.__addContactList:
            contact.addContactToFile()

    def listContacts(self):
        myfile = open('contacts.txt', 'r')
        ch = " "
        while ch:
            ch = myfile.readline()
            print(ch, end = " ")
        import os
        if os.stat("contacts.txt").st_size == 0:
            print("No contacts found!")
        print()
        print()
        myfile.close()

    def deleteAllContacts(self):
        myfile = open("contacts.txt", 'w')
        myfile.close()

    def deleteContact(self, name, email, phone):
        x = ["Name: ", str(name)]
        word1 = "".join(x)
        y = ["Email: ", str(email)]
        word2 = "".join(y)
        z = ["Phone no: ", str(phone)]
        word3 = "".join(z)
        lines = []
        found_sequence = False

        with open("contacts.txt", 'r') as file:
            for line in file:
                lines.append(line)

                if len(lines) >= 3:
                    if lines[-3].strip() == word1 and lines[-2].strip() == word2 and lines[-1].strip() == word3:
                        found_sequence = True
                        lines.pop()
                        lines.pop()
                        lines.pop()

        with open("contacts.txt", 'w') as file:
            for line in lines:
                file.write(line)

        if found_sequence:
            print("Successfully deleted contact!")
            print()
        else:
            print("Failed to find contact, please try again.")
            print()

    def search1(self, name, email, phone):
        x = ["Name: ", str(name)]
        word1 = "".join(x)
        target_word = word1

        input_file = "contacts.txt"

        with open(input_file, "r") as infile:
            lines = infile.readlines()

        for i, line in enumerate(lines):
            if target_word in line:
                print(line.rstrip())
                for j in range(i + 1, min(i + 3, len(lines))):
                    print(lines[j].rstrip())
        print()

    def search2(self, name, email, phone):
        y = ["Email: ", str(email)]
        word2 = "".join(y)
        target_word = word2

        input_file = "contacts.txt"

        with open(input_file, "r") as infile:
            lines = infile.readlines()

        for i, line in enumerate(lines):
            if target_word in line:
                found_target = True
                if i > 0:
                    print(lines[i - 1].rstrip())
                print(line.rstrip())
                if i < len(lines) - 1:
                    print(lines[i + 1].rstrip())
        print()

    def search3(self, name, email, phone):
        z = ["Phone no: ", str(phone)]
        word3 = "".join(z)

        target_word = word3
        input_file = "contacts.txt"

        with open(input_file, "r") as infile:
            lines = infile.readlines()

        for i, line in enumerate(lines):
            if target_word in line:
                found_target = True
                start_index = max(0, i - 2)
                for j in range(start_index, i):
                    print(lines[j].rstrip())
                print(line.rstrip())
        print()

    def searchContacts(self, name, email, phone):
        data_to_search = [name, email, phone]
        with open("contacts.txt", "r") as infile:
            file_contents = infile.read()

        if name in file_contents and email in file_contents and phone in file_contents:

            if name != "":
                if email == "":
                    if phone == "":
                        self.search1(name, email, phone)

            if name != "":
                if email != "":
                    if phone == "":
                        self.search1(name, email, phone)

            if name != "":
                if email == "":
                    if phone != "":
                        self.search1(name, email, phone)

            if name != "":
                if email != "":
                    if phone != "":
                        self.search1(name, email, phone)

            if name == "":
                if email != "":
                    if phone == "":
                        self.search2(name, email, phone)

            if name == "":
                if email != "":
                    if phone != "":
                        self.search2(name, email, phone)

            if name == "":
                if email == "":
                    if phone != "":
                        self.search3(name, email, phone)
        else:
            print("Failed to find contact, please try again.")
            print()

class Contact:
    name = None
    email = None
    phone = None

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def prettyPrint(self):
        print("""Name of contact: %s
            Email of contact: %s
            Phone number of contact: %s""" % (self.name, self.email, self.phone))

    def addContactToFile(self):
        myfile = open('contacts.txt', 'a')
        myfile.write("\n")
        myfile.write("""Name: %s
               Email: %s
               Phone no: %s""" % (self.name, self.email, self.phone))
        myfile.close()