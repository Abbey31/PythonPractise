to_do_list = []

def add_task():
    task = input("\nEnter the task to add:\n ")
    to_do_list.append(task)
    print(f"Task {task} added!")
        
    
def remove_task():
    task = input("\nEnter the task to remove:\n ")
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task {task} removed!")
    else:
        print(f"Task {task} not found!")
def view_tasks():
    if to_do_list:
        print("\nYour to_do_list:")
        for index, task in enumerate(to_do_list, 1):
            print(f"{index}. {task}")
    else:
        print("Your to do list is empty.")

while True:
    choice = input("press\n1 to add task:\n2 to remove task:\n3 to view_tasks:\nq to quit:\n")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice.lower() == "q":
        print("Goodbye!")
        break
    else:
        print("You must choose between 1,2 or 3 ")   
        continue

