name = "Musa"
count = 1

def another():
    color = "blue"
    global count
    count+= 1
    print(count)

def greeting(name):
    color = "red"
    print(color)
    print(name)
    

greeting("Sheu")



    greeting("Sheu")
another()