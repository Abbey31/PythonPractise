def generate():
    manipulate = {"A":1,"B":2,"C":3,"D":4}
    for value in manipulate.items():
        print(generate())
def edit():
    answer = input("pick between A, B or C ")
    if answer == "A".upper():
        print(generate())
    elif answer == "B".upper():
        print(generate())
    else:
        print(generate())
edit()