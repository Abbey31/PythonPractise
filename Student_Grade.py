print("Welcome to the school board!")  

students_grade = {}  


student_name = input("Enter your name:\n")  
  
if student_name not in students_grade:  
      
    students_grade[student_name] = {}  

  
while True:  
    subject = input("Enter your subject (or type 'exit' to stop adding subjects):\n")  
    if subject.lower() == 'exit':  
        break    
    
    grade = input("Enter your grade for {}:\n".format(subject))  
    
     
    students_grade[student_name][subject] = grade  

print("========================================")

print("\nStudent Grades:")  
for student, subjects in students_grade.items():  
    print(f"\n{student}:")  
    for subject, grade in subjects.items():  
        print(f"  {subject}: {grade}")
print("========================================")
        