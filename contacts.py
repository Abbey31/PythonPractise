contact_book = {}  

def add_contact():    
    name = input('Enter contact name: ')  
    phone = input('Enter phone number: ')  # Changed to input to keep it as a string  
    email = input('Enter e-mail address: ')  

    if name in contact_book:  
        print('Contact already exists!')  
    else:  
        contact_book[name] = {"phone": phone, "email": email}  # Changed "e-mail" to "email"  
        print(f'Contact {name} added successfully')  

def search_contact():  
    name = input('Enter the name you want to search: ')  
    if name in contact_book:  
        print(f"Name: {name}, Phone: {contact_book[name]['phone']}, Email: {contact_book[name]['email']}")  # Changed to "email"  
    else:  
        print('Not Found')  

def edit_contact():  
    name = input("Enter the name you want to edit: ")  
    if name in contact_book:  
        phone = input("Enter new phone number: ")  
        email = input("Enter new email address: ")  
        contact_book[name] = {"phone": phone, "email": email}  # Maintain consistency  
        print(f"Contact {name} updated successfully")  
    else:  
        print("Contact not found.")  

def delete_contact():  
    name = input("Enter the name of the contact you want to delete: ")  
    if name in contact_book:  
        del contact_book[name]  
        print(f"Contact {name} deleted successfully.")  
    else:  
        print("Contact not found.") 

def view_all_contacts():
    if contact_book:
        for name, details in contact_book.items():
            print(f"Name:{name}, phone:{details['phone']},email:{details['email']}")
    else:
        print("Contact book is empty") 


while True:
    print("\n-----------Contact Book Menu---------")
    print("1.Add a new Contact.")
    print("2.Search Contact")
    print("3.Edit a Contact")
    print("4.Delete a Contact")
    print("5.View all contacts")
    print("6.Exit")

    answer = input("Enter your choice (1-6): ")
    if answer == "1":
        add_contact()
    elif answer == "2":
        search_contact()
    elif answer == "3":
        edit_contact()
    elif answer == "4":
        delete_contact()
    elif answer == "5":
        view_all_contacts()
    elif answer == "6":
        print("Exiting Bye!👋")
        break
    else:
        print("Invalid choice Try again.")

    
