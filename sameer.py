# Dictionary
python_dict = {
    "name": "Python",
    "version": 3.12,
    "description": "High Level Programming Language",
    "level": "Beginner"
}
#result = python_dict.get('description')
#print(result)
result = python_dict.pop('level')
print(result)
print(python_dict)
