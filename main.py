import tkinter as tk
from tkinter import messagebox
import json
import os
import numpy

class Product:
    def init(self, name, price):
        self.name = name
        self.price = price

class InvoiceItem:
    def init(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Customer:
    def init(self, name, email):
        self.name = name
        self.email = email

class BillingApp:
    def init(self, root):
        self.root = root
        self.root.title("Billing System")

        self.products = []
        self.invoice_items = []
        self.customers = []

        # Load existing data from files
        self.load_data()

        # Create a label for product name
        self.label_product = tk.Label(root, text="Product Name:")
        self.label_product.pack()

        # Create an entry for product name
        self.entry_product = tk.Entry(root)
        self.entry_product.pack()

        # Create a label for product price
        self.label_price = tk.Label(root, text="Price:")
        self.label_price.pack()

        # Create an entry for product price
        self.entry_price = tk.Entry(root)
        self.entry_price.pack()

        # Create a label for quantity
        self.label_quantity = tk.Label(root, text="Quantity:")
        self.label_quantity.pack()

        # Create an entry for quantity
        self.entry_quantity = tk.Entry(root)
        self.entry_quantity.pack()

        # Create a button to add a product
        self.add_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_button.pack()

        # Create a listbox to display added products
        self.product_listbox = tk.Listbox(root)
        self.product_listbox.pack()

        # Create a label for customer name
        self.label_customer_name = tk.Label(root, text="Customer Name:")
        self.label_customer_name.pack()

        # Create an entry for customer name
        self.entry_customer_name = tk.Entry(root)
        self.entry_customer_name.pack()

        # Create a label for customer email
        self.label_customer_email = tk.Label(root, text="Customer Email:")
        self.label_customer_email.pack()

        # Create an entry for customer email
        self.entry_customer_email = tk.Entry(root)
        self.entry_customer_email.pack()

        # Create a button to add a customer
        self.add_customer_button = tk.Button(root, text="Add Customer", command=self.add_customer)
        self.add_customer_button.pack()

        # Create a label to display the customer's details
        self.label_customer_details = tk.Label(root, text="")
        self.label_customer_details.pack()

        # Create a button to generate an invoice
        self.generate_button = tk.Button(root, text="Generate Invoice", command=self.generate_invoice)
        self.generate_button.pack()

        # Create a label to display the total amount
        self.label_total = tk.Label(root, text="")
        self.label_total.pack()

        # Create a button to save data
        self.save_button = tk.Button(root, text="Save Data", command=self.save_data)
        self.save_button.pack()

    def add_product(self):
        name = self.entry_product.get()
        price = float(self.entry_price.get())
        quantity = int(self.entry_quantity.get())

        product = Product(name, price)
        item = InvoiceItem(product, quantity)

        self.products.append(product)
        self.invoice_items.append(item)

        self.product_listbox.insert(tk.END, f"{name} - ${price:.2f} x {quantity}")

        # Clear input fields
        self.entry_product.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def add_customer(self):
        name = self.entry_customer_name.get()
        email = self.entry_customer_email.get()

        customer = Customer(name, email)
        self.customers.append(customer)

        self.label_customer_details.config(text=f"Customer: {name} ({email})")
      # Clear input fields
        self.entry_customer_name.delete(0, tk.END)
        self.entry_customer_email.delete(0, tk.END)

    def generate_invoice(self):
        if not self.invoice_items:
            messagebox.showinfo("Error", "No items in the invoice.")
            return

        total = sum(item.product.price * item.quantity for item in self.invoice_items)
        customer_details = self.label_customer_details.cget("text")

        if not customer_details:
            messagebox.showinfo("Error", "Please add a customer.")
            return

        messagebox.showinfo("Invoice", f"Invoice for {customer_details}\nTotal Amount: ${total:.2f}")

    def save_data(self):
        data = {
            "products": [(p.name, p.price) for p in self.products],
            "customers": [(c.name, c.email) for c in self.customers],
        }

        with open("billing_data.json", "w") as file:
            json.dump(data, file)

        messagebox.showinfo("Saved", "Data has been saved to billing_data.json")

    def load_data(self):
        if os.path.exists("billing_data.json"):
            with open("billing_data.json", "r") as file:
                data = json.load(file)

            for name, price in data["products"]:
                self.products.append(Product(name, price))

            for name, email in data["customers"]:
                self.customers.append(Customer(name, email))

def main():
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()

if name == "main":
    main()
