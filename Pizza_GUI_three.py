import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#Heading of the GUI
Heading = ttk.Label(root, text = "Dream Pizza", padding = 15, font = 10)
Heading.grid(row = 0, column = 0)

#Customer Details if order is for delivery
NameLabel = ttk.Label(root, text = "Name")
NameLabel.grid(row = 1, column = 0)

AddressLabel = ttk.Label(root, text = "Address")
AddressLabel.grid(row = 2, column = 0)

PhoneLabel = ttk.Label(root, text = "Phone Number")
PhoneLabel.grid(row = 3, column = 0)

#Customer Details if order is for delivery
Name_entry = ttk.Entry(root)
Name_entry.grid(row = 1, column = 1)

Address_entry = ttk.Entry(root)
Address_entry.grid(row = 2, column = 1)

PhoneNumber_entry = ttk.Entry(root)
PhoneNumber_entry.grid(row = 3, column = 1)

#Button widget to go to next page
nextButton = ttk.Button(root, text = "Next")
nextButton.grid(row = 8, column = 1)

root.mainloop()