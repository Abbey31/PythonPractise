master_pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input('Account Name: ')
    pwd = input('password: ')

    with open('passwords.txt', 'a') as  f:
    
while True:
    mode = input("Would you like to add a new password or view the existing ones (view/add)? ")
    if mode == "q":
        break

    if mode == "view":
        view()
     
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue