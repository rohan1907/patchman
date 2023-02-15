import tkinter as tk
import json
from tkinter import messagebox

#to patch to test server

class Option1Screen(tk.Tk):
    def __init__(self, parent):
        super().__init__()

        self.title("Test Servers Patch")

        self.parent = parent

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack()

        # Create the Test Server field
        self.test_server_label = tk.Label(self, text="Test Server:")
        self.test_server_label.pack()
        self.test_server_var = tk.StringVar(self)
        self.test_server_dropdown = tk.OptionMenu(self, self.test_server_var, "Test Server 2", "Test Server 4")
        self.test_server_dropdown.pack()

        #Create insta version dropdown field
        self.insta_version_label = tk.Label(self, text="Insta Version:")
        self.insta_version_label.pack()
        self.insta_version_var = tk.StringVar(self)
        self.insta_version_dropdown = tk.OptionMenu(self, self.insta_version_var, "Insta 12.4", "Insta 12.5")
        self.insta_version_dropdown.pack()



        # Create the List of Files Changed field
        self.files_changed_label = tk.Label(self, text="List of Files Changed:")
        self.files_changed_label.pack()
        self.files_changed_entry = tk.Text(self)
        self.files_changed_entry.pack()


        # Create the Tomcat Restart Required checkbox
        self.tomcat_restart_label = tk.Label(self, text="Tomcat Restart Required:")
        self.tomcat_restart_label.pack()
        self.tomcat_restart_var = tk.BooleanVar(self)
        self.tomcat_restart_checkbox = tk.Checkbutton(self, variable=self.tomcat_restart_var)
        self.tomcat_restart_checkbox.pack()

        # Create the Save button
        self.save_button = tk.Button(self, text="Save", command=print("hello"))
        self.save_button.pack()

    def go_back(self):
        self.destroy()
        self.parent.deiconify()


