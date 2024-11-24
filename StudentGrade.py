StudentNames = []  
Subject = []  
Grade = []  
studentCount = 0  

print("Welcome to the school board!")  
while True:  
    name = input("Enter your student name (or type 'exit' to stop adding subjects):\n")  
    if name.lower() == 'exit':  
        break  
    StudentNames.append(name)    
    
    subject = input("Enter your subject (or type 'exit' to stop adding subjects):\n")  
    if subject.lower() == 'exit':  
        break  
    Subject.append(subject)  
    

    grade = input("Enter your grade (or type 'exit' to stop adding subjects):\n")  
    if grade.lower() == 'exit':  
        break  
    Grade.append(grade)  
    studentCount += 1  

print("========================================")   
print("{:<10} {:<10} {:<5}".format("Name", "Subject", "Grade"))  
print("----------------------------------------")  
for i in range(studentCount):  
    print("{:<10} {:<10} {:<5}".format(StudentNames[i], Subject[i], Grade[i]))  

print("========================================")