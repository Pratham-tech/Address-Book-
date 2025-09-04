import tkinter as tk
from tkinter import messagebox, Toplevel
import consoleInputManager

class AddressBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contacts Address Book")
        self.manager = consoleInputManager.ConsoleInputManager()

        self.title_label = tk.Label(root, text="Contacts Address Book", font=("Aptos Display", "18", "bold"))
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(root, text=" What do you want to do? Please click a button...", font = ("Aptos Display", "12", "italic"))
        self.instruction_label.pack(anchor="w")

        empty_label = tk.Label(root, text="")
        empty_label.pack()
        empty_label = tk.Label(root, text="")
        empty_label.pack()

        self.create_button("List Contacts", "   Lists all saved contacts")
        empty_label = tk.Label(root, text="")
        empty_label.pack()
        
        self.create_button("Add Contact", "   Adds a contact")
        empty_label = tk.Label(root, text="")
        empty_label.pack()
        
        self.create_button("Delete Contact", "   Deletes a contact")
        empty_label = tk.Label(root, text="")
        empty_label.pack()
        
        self.create_button("Delete All Contacts", "   Deletes all contacts")
        empty_label = tk.Label(root, text="")
        empty_label.pack()
        
        self.create_button("Search Contacts", "   Searches for a contact")
        empty_label = tk.Label(root, text="")
        empty_label.pack()
        
        self.create_button("Close", "   Closes the address book")

    def create_button(self, text, description):
        button_frame = tk.Frame(self.root)
        button_frame.pack(anchor="w", padx=10, pady=5)

        button = tk.Button(button_frame, text=text, command=lambda t=text: self.button_action(t), width=20, borderwidth=2, relief="solid")
        button.pack(side="left")

        desc_label = tk.Label(button_frame, text=description)
        desc_label.pack(side="left")

    def button_action(self, button_text):
        if button_text == "List Contacts":
            self.list_contacts()
        elif button_text == "Add Contact":
            self.open_add_contact_window()
        elif button_text == "Delete Contact":
            self.open_delete_contact_window()
        elif button_text == "Delete All Contacts":
            self.delete_all_contacts()
        elif button_text == "Search Contacts":
            self.open_search_contacts_window()
        elif button_text == "Close":
            self.root.destroy()  

    def list_contacts(self):
        contacts = self.manager.contactManager.listContacts()

    def open_add_contact_window(self):
        add_window = Toplevel(self.root)
        add_window.title("Add Contact")
        add_window.geometry("400x300")

        self.name_label = tk.Label(add_window, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(add_window)
        self.name_entry.pack()

        self.email_label = tk.Label(add_window, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(add_window)
        self.email_entry.pack()

        self.phone_label = tk.Label(add_window, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(add_window)
        self.phone_entry.pack()

        self.add_button = tk.Button(add_window, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if name and email and phone:
            self.manager.contactManager.addContact(name, email, phone)
            messagebox.showinfo("Success", "Contact added successfully!")

            print("Contact added successfully!")

            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def open_delete_contact_window(self):
        delete_window = Toplevel(self.root)
        delete_window.title("Delete Contact")
        delete_window.geometry("400x300")

        self.name_label = tk.Label(delete_window, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(delete_window)
        self.name_entry.pack()

        self.email_label = tk.Label(delete_window, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(delete_window)
        self.email_entry.pack()

        self.phone_label = tk.Label(delete_window, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(delete_window)
        self.phone_entry.pack()
        
        self.delete_button = tk.Button(delete_window, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def delete_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        import os
        initial_size = os.path.getsize("contacts.txt")
    
        if name and email and phone:
            contact_deleted = self.manager.contactManager.deleteContact(name, email, phone)

            final_size = os.path.getsize("contacts.txt")
    
            if initial_size != final_size:
                messagebox.showinfo("Success", "Contact deleted successfully!")
                print("Contact deleted successfully!")
                self.name_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Failed to find contact, please try again.")
                print("Failed to find contact, please try again.")
        else:
            messagebox.showerror("Error", "Please provide all three search criteria.")

    def delete_all_contacts(self):
        confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all contacts?")
    
        if confirmation:
            self.manager.contactManager.deleteAllContacts()
            messagebox.showinfo("Success", "All contacts deleted successfully!")
            print("All contacts deleted successfully!")
        else:
            pass

    def open_search_contacts_window(self):
        search_window = Toplevel(self.root)
        search_window.title("Search Contacts")
        search_window.geometry("400x300")

        self.name_label = tk.Label(search_window, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(search_window)
        self.name_entry.pack()

        self.email_label = tk.Label(search_window, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(search_window)
        self.email_entry.pack()

        self.phone_label = tk.Label(search_window, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(search_window)
        self.phone_entry.pack()

        self.search_button = tk.Button(search_window, text="Search Contacts", command=self.search_contacts)
        self.search_button.pack()

    def search_contacts(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if name or email or phone:
            contacts = self.manager.contactManager.searchContacts(name, email, phone)
            with open("contacts.txt", "r") as infile:
                file_contents = infile.read()
            if name in file_contents and email in file_contents and phone in file_contents:
                pass
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please provide at least one search criteria.")

def main():
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
