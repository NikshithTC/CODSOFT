import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = {}
        
        # Create GUI components
        self.create_widgets()
        
    def create_widgets(self):
        # Labels and Entry widgets
        tk.Label(self.root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Phone Number:").grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1)
        
        tk.Label(self.root, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1)
        
        tk.Label(self.root, text="Address:").grid(row=3, column=0)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1)
        
        # Buttons
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2)
        
        # Contact Listbox
        self.contact_listbox = tk.Listbox(self.root)
        self.contact_listbox.grid(row=9, column=0, columnspan=2, sticky="nsew")
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone Number are required.")
        
        self.clear_entries()
    
    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for name in self.contacts:
            self.contact_listbox.insert(tk.END, f"{name} - {self.contacts[name]['phone']}")
    
    def search_contact(self):
        search_name = self.name_entry.get()
        if search_name in self.contacts:
            contact = self.contacts[search_name]
            messagebox.showinfo("Contact Found", f"Name: {search_name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
        else:
            messagebox.showerror("Error", "Contact not found.")
    
    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            contact = self.contacts[name]
            contact['phone'] = self.phone_entry.get()
            contact['email'] = self.email_entry.get()
            contact['address'] = self.address_entry.get()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")
        
        self.clear_entries()
    
    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Contact not found.")
        
        self.clear_entries()
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
