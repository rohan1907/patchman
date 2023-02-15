import tkinter as tk
from option1_screen import Option1Screen
from option2_screen import Option2Screen

class EntryScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.title("Select type of patch")

        # Create UI elements
        tk.Label(self, text="Please choose an option:").grid(row=0, column=0, padx=10, pady=10)

        # Option 1 button
        tk.Button(self, text="Test Server Patch", command=self.show_option1).grid(row=1, column=0, padx=10, pady=10)

        # Option 2 button
        tk.Button(self, text="Customer Patch", command=self.show_option2).grid(row=2, column=0, padx=10, pady=10)

    def show_option1(self):
        self.option1_screen = Option1Screen(self)
        self.withdraw()
        self.option1_screen.mainloop()
        self.deiconify()

    def show_option2(self):
        self.option2_screen = Option2Screen(self)
        self.withdraw()
        self.option2_screen.mainloop()
        self.deiconify()
