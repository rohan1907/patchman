import tkinter as tk
import json
import FileSegregator
class Option2Screen(tk.Tk):
    def __init__(self, parent):
        super().__init__()

        self.title("Customer Patch ")

        self.parent = parent

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack()

        # Create the Test Server field
        self.test_server_label = tk.Label(self, text="Test Server:")
        self.test_server_label.pack()
        self.test_server_var = tk.StringVar(self)
        self.test_server_dropdown = tk.OptionMenu(self, self.test_server_var, "Test Server 2", "Test Server 4")
        self.test_server_dropdown.pack()

        # Create the Customer Schema Name field
        self.customer_schema_label = tk.Label(self, text="Customer Schema Name:")
        self.customer_schema_label.pack()
        self.customer_schema_entry = tk.Entry(self)
        self.customer_schema_entry.pack()

        # Create the List of Files Changed field
        self.files_changed_label = tk.Label(self, text="List of Files Changed:")
        self.files_changed_label.pack()
        self.files_changed_entry = tk.Text(self)
        self.files_changed_entry.pack()

        # Create the Ticket Number field
        self.ticket_number_label = tk.Label(self, text="Ticket Number:")
        self.ticket_number_label.pack()
        self.ticket_number_entry = tk.Entry(self)
        self.ticket_number_entry.pack()

        # Create the Username field
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # Create the Tomcat Restart Required checkbox
        self.tomcat_restart_label = tk.Label(self, text="Tomcat Restart Required:")
        self.tomcat_restart_label.pack()
        self.tomcat_restart_var = tk.BooleanVar(self)
        self.tomcat_restart_checkbox = tk.Checkbutton(self, variable=self.tomcat_restart_var)
        self.tomcat_restart_checkbox.pack()

        # Create the Save button
        self.save_button = tk.Button(self, text="Save", command=self.save_data)
        self.save_button.pack()

    def go_back(self):
        self.destroy()
        self.parent.deiconify()

    def save_data(self):
        filesPathInTestServer = FileSegregator.segregate_files(self.files_changed_entry.get("1.0", tk.END), "12.4")
        data = {
            "schema_name": self.customer_schema_entry.get(),
            "file_paths": filesPathInTestServer,
            "JIRA_ID": self.ticket_number_entry.get(),
        }

        with open(str(self.ticket_number_entry.get())+".json", "w") as f:
            json.dump(data, f)

        tk.messagebox.showinfo("Success", "Data saved successfully!")
        self.destroy()
        self.parent.deiconify()
