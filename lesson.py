# # # String data type

# # #literal assignment
# # first = "Dave"
# # last = "Gray"

# # # print(type(first))
# # # print(type(first) == str)
# # # print(isinstance(first,str))

# # #Constructor Function
# # # pizza = str("Pepperoni")
# # # print(type(pizza))
# # # print(type(pizza) == str)
# # # print(isinstance(pizza,str))

# # #String Concatenation
# # # fullname = first + " " + last
# # # print(fullname)

# # # fullname += "!"
# # # print(fullname)

# # # decade = str(1980)
# # # print(type(decade))
# # # print("I love rock music from the "+decade+'s')

# # # String Methods
# # # print(first)
# # # print(first.lower())
# # # print(first.upper())
# # # print(first)
# # #LISTS
# # users = ['Dave','John','Sara']
# # data = ['Dave',42, True]
# # emptylist = []
# # print("Dave" in emptylist)
# # print(users[-2])

# # # print(users[0:2])
# # # print(users[1:])
# # # print(users[-3:-1])

# # # print(len(data))

# # # users.append('Elsa')
# # # print(users)

# # # users += ['Jason']
# # # print(users)
# # # users.extend(['Robert','Jimmy'])
# # # print(users)

# # # users.extend(data)
# # # print(users)

# # users.insert(0,'Bob')
# # print(users)

# # users[2:2] = ['Eddie','Alex']
# # print(users)

# # users[1:3] = ['Robert','JPJ']
# # print(users)

# # users.remove('Bob')
# # print(users)
# # print(users.pop())

# # data.clear()
# # print(data)

# # users[1:2] = ['dave']
# # users.sort()
# # print(users)

# # users.sort(key=str.lower)
# # print(users)

# # nums = [4,42,78,1,5]
# # nums.reverse()
# # print(nums)

# #nums.sort(reverse=True)
# #print(nums)

# # print(sorted(nums, reverse=True))
# # print(nums)

# # numscopy = nums.copy()
# # mynums = list(nums)
# # mycopy = nums[:]

# # print(numscopy)
# # print(mynums)
# # print(mycopy.sort())
# # print(mycopy)
# # print(nums)

# # print(type(nums))

# # mylist = list([1,"Neil",True])
# # print(mylist) 
# #TUPLES
# # mytuple = tuple(('Dave',42, True))

# # anothertuple = (1,4,2,8)

# # print(mytuple)
# # print(type(mytuple))
# # print(type(anothertuple))

# # newlist = list(mytuple)
# # newlist.append('Neil')
# # newtuple = tuple(newlist)
# # print(newtuple)

# # (one,*two, hey) = anothertuple
# # print(one)
# # print(two)
# # print(hey)

# # print(anothertuple.count(2))
# # Dictionaries
# band = {
#     "vocals":"Plant",
#     "guitar":"Page"
# }
# band2 = dict(vocals="Plant",guitar="Page")
# print(band)
# print(band2)
# print(type(band))
# print(len(band))
# print(band.get("guitar"))

# # List all Keys
# print(band.keys())
# # List all values
# print(band.values())
# #List of key/value pairs as tuples
# print(band.items())
# #Verify a key exists
# print("guitar" in band)
# print("triangle" in band)

# # Change values
# band["vocals"] = "Coverdale"
# band.update({"bass":"JPJ"})
# print(band)
# #Remove items
# print(band.pop("bass"))
# print(band)
# #Add a new value
# band["drums"] = "Bonham"
# print(band)
# #Remove an item again
# #NOTE:POP() returns tuple
# print(band.popitem())
# print(band)

# #Delete and clear
# band["drums"] = "Bonham"
# del(band["drums"])
# print(band)

# band2.clear()
# print(band2)

# # Copy Dictionaries
# # band2 = band # create a reference
# # print("Bad copy!")
# # print(band2)
# # print(band)
# # band2["drums"] = "Dave"
# # print(band)
# band2 = band.copy()
# band2["drums"] = "Dave"
# print(band)
# print(band2)

# #or use the dict() constructor function
# band3 = dict(band)
# print("Good copy!")
# print(band3)
# #Nested dictionaries

# member1 = {
#     "name":"Plant",
#     "instrument":"vocals"
# }
# member2 = {
#     "name":"Page",
#     "instrument":"guitar"    
# }
# band = {
#     "member1":member1,
#     "member2":member2
# }
# print(band)
# print(band["member1"]["name"])

# Sets
# nums = {1,2,3,4}

# nums2 = set((1,2,3,4))
# print(nums)
# print(nums2)
# print(type(nums))
# print(len(nums))
# #No duplicate allowed
# print(nums)
# #True is a dupe of 1, False is a dupe of zero
# nums = {1,True,2,False,3,4,0}
# print(nums)  
# #Check if a value is in a set
# print(2 in nums)

# # but you cannot refer to an element in the set with an index position or key

# # Add a new element to a set
# nums.add(8)
# print(nums)

# # Add elements from one set to another
# morenums = [5,6,7]
# nums.update(morenums)
# print(nums)

# # you can use update with lists,tuples, and dictionaries, too

# # Merge two sets to create a new set
# one = {1,2,3}
# two = {5,6,7}

# mynewset = one.union(two)
# print(mynewset)

# # Keep only duplicates
# one = {1,2,3}
# two = {2,3,4}

# one.intersection_update(two)
# print(one)

# # Keep everything except the duplicates
# one = {1,2,3}
# two = {2,3,4}

# one.symmetric_difference_update(two)
# print(one)
#LOOPS

# value = 1
# while value <= 10:
#     print(value)
#     if value ==5:
#         break
#     value += 1
# value = 1
# while value <= 10:
#     value += 1
#     if value ==5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))
#FOR LOOPS
#for x in "Mississippi":
 #   print(x)


#names = ["Dave","Sara","John"]
#for x in names:
 #   if x == "Sara":
#        break
 #   print(x)
#for x in names:
 #   if x == "Sara":
  #      continue
   # print(x)
# ranges
#for x in range(4):
 #   print(x)

#for x in range(2,4):
 #   print(x)
#for x in range(5):
 #   print(x)
# for x in range(0,101,5):
#     print(x)
# else:
#     print("Glad that\'s over")

# names = ["Dave","Sara","John"]
# actions = ["codes","eats","sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")
# for action in actions:
#     for name in names:
#         print(name + " " + action + ".")
# FUNCTIONS
#def hello():
 #    print("Hello World!")
     
#hello()
# def sum(num1,num2):
#       print(num1+num2)
    
# total = sum(2,3)
# def sum(num1,num2):
#       print(num1+num2)
    
#total = sum(2,3)
# def sum(num1=0,num2=0):
#       if (type(num1) is not int or type(num2) is not int):
#             return num1 + num2
    
#total = sum(2,3)
#print(total)
# def sum(num1,num2):
#       print(num1+num2)
    
# total = sum(2,3)
 
 #RECURSION
def add_one(num):
    if(num >= 9):
        return num + 1
    
    total = num + 1
    print(total)

    return add_one(total)

mynewtotal = add_one(0)
print(mynewtotal)




