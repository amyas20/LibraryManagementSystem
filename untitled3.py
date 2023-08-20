# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 08:27:36 2023

@author: oguru
"""

# Inventory Management System
1
# User data
users = [
    {"username": "admin", "password": "admin123", "level": "admin"},
    {"username": "user", "password": "user123", "level": "user"}
]

# Inventory data
inventory = [
    {"id": 1, "name": "Croissant", "quantity": 10, "price": 2.99},
    {"id": 2, "name": "Baguette", "quantity": 5, "price": 1.99},
    {"id": 3, "name": "Muffin", "quantity": 8, "price": 1.49},
    {"id": 4, "name": "Cupcake", "quantity": 15, "price": 2.49},
    {"id": 5, "name": "Bread Roll", "quantity": 20, "price": 0.99},
    {"id": 6, "name": "Danish Pastry", "quantity": 12, "price": 3.49},
    {"id": 7, "name": "Scone", "quantity": 7, "price": 1.79},
    {"id": 8, "name": "Pretzel", "quantity": 10, "price": 1.99},
    {"id": 9, "name": "Cinnamon Roll", "quantity": 6, "price": 2.99},
    {"id": 10, "name": "Eclair", "quantity": 4, "price": 3.99},
    {"id": 11, "name": "Donut", "quantity": 18, "price": 1.29},
    {"id": 12, "name": "Apple Pie", "quantity": 3, "price": 4.99},
    {"id": 13, "name": "Cheesecake", "quantity": 5, "price": 5.49},
    {"id": 14, "name": "Brownie", "quantity": 9, "price": 1.99},
    {"id": 15, "name": "Custard Tart", "quantity": 6, "price": 2.49}
]

# Purchase report data
purchase_report = []

# Login function
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            return user["level"]

    return None

# Admin level functions
def show_all_products():
    print("All Bakery Products:")
    print("ID\tName\tQuantity\tPrice")

    for product in inventory:
        print(f"{product['id']}\t{product['name']}\t{product['quantity']}\t{product['price']}")

def display_product_details():
    product_id = int(input("Enter the product ID: "))

    for product in inventory:
        if product["id"] == product_id:
            print("Product Details:")
            print("ID\tName\tQuantity\tPrice")
            print(f"{product['id']}\t{product['name']}\t{product['quantity']}\t{product['price']}")
            return

    print("Product not found.")

def add_update_product():
    product_id = int(input("Enter the product ID: "))

    for product in inventory:
        if product["id"] == product_id:
            print("Product found. Enter new details (leave blank to skip):")
            name = input(f"Enter new name ({product['name']}): ")
            quantity = input(f"Enter new quantity ({product['quantity']}): ")
            price = input(f"Enter new price ({product['price']}): ")

            if name:
                product["name"] = name
            if quantity:
                product["quantity"] = int(quantity)
            if price:
                product["price"] = float(price)

            print("Product details updated.")
            return

    print("Product not found.")

def delete_product():
    product_id = int(input("Enter the product ID: "))

    for product in inventory:
        if product["id"] == product_id:
            inventory.remove(product)
            print("Product deleted.")
            return

    print("Product not found.")

def display_purchase_report():
    print("Purchase Report:")
    print("Product\tQuantity\tTotal Price")

    for item in purchase_report:
        product = item["product"]
        quantity = item["quantity"]
        total_price = quantity * product["price"]
        print(f"{product['name']}\t{quantity}\t{total_price}")

# User level functions
def display_user_purchase_report():
    print("User Purchase Report:")
    print("Product\tQuantity\tTotal Price")

    for item in purchase_report:
        product = item["product"]
        quantity = item["quantity"]
        total_price = quantity * product["price"]
        print(f"{product['name']}\t{quantity}\t{total_price}")

def generate_bill():
    total_price = 0

    for item in purchase_report:
        product = item["product"]
        quantity = item["quantity"]
        total_price += quantity * product["price"]

    print("Bill:")
    print("Product\tQuantity\tPrice\tTotal Price")

    for item in purchase_report:
        product = item["product"]
        quantity = item["quantity"]
        total_item_price = quantity * product["price"]
        print(f"{product['name']}\t{quantity}\t{product['price']}\t{total_item_price}")

    print(f"Total Price: {total_price}")

def buy_product():
    product_id = int(input("Enter the product ID: "))
    quantity = int(input("Enter the quantity to buy: "))

    for product in inventory:
        if product["id"] == product_id:
            if product["quantity"] >= quantity:
                product["quantity"] -= quantity

                purchase_report.append({"product": product, "quantity": quantity})
                print("Purchase successful.")
            else:
                print("Insufficient quantity.")
            return

    print("Product not found.")

# Admin level menu
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Show All Bakery Products")
        print("2. Display Product Details")
        print("3. Add/Update Product")
        print("4. Delete Product")
        print("5. Display Purchase Report")
        print("6. Logout")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_all_products()
        elif choice == "2":
            display_product_details()
        elif choice == "3":
            add_update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            display_purchase_report()
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

# User level menu
def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Display User Purchase Report")
        print("2. Generate Bill")
        print("3. Buy Bakery Product")
        print("4. Logout")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_user_purchase_report()
        elif choice == "2":
            generate_bill()
        elif choice == "3":
            buy_product()
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

# Opening page
print("Welcome to the Bakery Inventory Management System!")
print("Please select your level:")
print("1. Admin")
print("2. User")

level = input("Enter your choice (1 or 2): ")

if level == "1":
    user_level = login()
    if user_level == "admin":
        print("Logged in as admin.")
        admin_menu()
    else:
        print("Invalid username or password. Access denied.")

elif level == "2":
    user_level = login()
    if user_level == "user":
        print("Logged in as user.")
        user_menu()
    else:
        print("Invalid username or password. Access denied.")

else:
    print("Invalid choice. Please try again.")