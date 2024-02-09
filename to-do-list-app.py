import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        """
        Initialize the App.

        Parameters:
        - root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("To-Do List")

        # Create an instance of UpdatableList
        self.updatable_list = UpdatableList()

        # Initialize and configure the Listbox
        self.listbox = tk.Listbox(root)
        self.listbox.pack(padx=20, pady=20)

        # Populate the Listbox with current items
        self.update_listbox()

        # Initialize and configure the Entry widget
        self.entry = tk.Entry(root)
        self.entry.pack(pady=15)

        # Create "Add" button
        add_button = tk.Button(root, text="Add", command=self.add_item)
        add_button.pack()

        # Create "Remove" button
        remove_button = tk.Button(root, text="Remove", command=self.remove_item)
        remove_button.pack()

    def update_listbox(self):
        """
        Update the Listbox with items from UpdatableList.
        """
        self.listbox.delete(0, tk.END)
        for item in self.updatable_list.item_list:
            self.listbox.insert(tk.END, item)

    def add_item(self):
        """
        Add a new item to the list and update the Listbox.
        """
        new_item = self.entry.get()
        if new_item:
            self.updatable_list.add_item(new_item)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter an item to add.")

    def remove_item(self):
        """
        Remove the selected item from the list and update the Listbox.
        """
        selected = self.listbox.curselection()
        if selected:
            item = self.listbox.get(selected[0])
            self.updatable_list.remove_item(item)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Select an item to remove.")

class UpdatableList:
    def __init__(self):
        """
        Initialize UpdatableList with a list of items loaded from a file.
        """
        self.item_list = self.load_list()

    def load_list(self):
        """
        Load the list of items from a file.

        Returns:
        - list: List of items.
        """
        try:
            with open("list.txt", "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []

    def save_list(self):
        """
        Save the current list to a file.
        """
        with open("list.txt", "w") as file:
            for item in self.item_list:
                file.write(item + "\n")

    def add_item(self, item):
        """
        Add a new item to the list.

        Parameters:
        - item (str): The item to be added.
        """
        self.item_list.append(item)
        self.save_list()

    def remove_item(self, item):
        """
        Remove an item from the list.

        Parameters:
        - item (str): The item to be removed.
        """
        if item in self.item_list:
            self.item_list.remove(item)
            self.save_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

