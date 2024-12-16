from food_item import Food_Item
from menu import Menu
from order import Order
from restaurant import Restaurant
from user import Admin,Customer,Employee

mamar_res = Restaurant("MAMA")
def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Pay bill")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))

        if(choice == 1):
            customer.view_menu(mamar_res)
        elif(choice == 2):
            item_name = input("Enter Your Item Name: ")
            item_quantity = int(input("Enter Item Quantity: "))
            customer.add_to_cart(mamar_res,item_name,item_quantity)
        elif(choice == 3):
            customer.view_cart()
        elif(choice == 4):
            customer.pay_bill()
        elif(choice == 5):
            break
        else:
            print("Invalid Input")

def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. View item")
        print("5. Delete item")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))

        if(choice == 1):
            item_name = input("Enter the item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = Food_Item(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_res,item)
        elif(choice == 2):
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            address = input("Enter employee address: ")
            phone = input("Enter employee phone: ")
            designation = input("Enter employee designation: ")
            age = input("Enter employee age: ")
            salary = input("Enter employee salary: ")
            admin.add_employees(mamar_res,name, phone, email, address,age,designation,salary)
        elif(choice == 3):
            admin.view_employee(mamar_res)
        elif(choice == 4):
            admin.view_menu(mamar_res)
        elif(choice == 5):
            del_item = input("Enter your item: ")
            admin.delete_item(mamar_res,del_item)
        elif(choice == 6):
            break
        else:
            print("Invalid Input")

while True:
    print("----Welcome----")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input('Enter your choice: '))

    if(choice == 1):
        customer_menu()
    elif(choice == 2):
        admin_menu()
    elif(choice == 3):
        break
    else:
        print("Invalid choice")