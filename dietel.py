
# # # # # roman_numerals = {'I':1, 'II':2,'III':3,'V':5,'X':100}
# # # # # roman_numerals['L'] = 50
# # # # # res = roman_numerals.get("I")
# # # # # print(roman_numerals)
# # # # # print(res)
# # # # months = {'January':1,'February':2,'March':3}
# # # # #for month_name in months.keys():
# # # #     #print(month_name, end=' ')
# # # # #for month_name in months.values():
# # # #  #   print(month_name, end=' ')
# # # # months_view = months.keys()
# # # # for key in months_view:
# # # #     print(key, end=' ')
# # # # months['December'] = 12
# # # # print(months)
# # # # #for key in months_view:
# # # # #    print(key, end=" ")
# # # # #print(list(months.values()))
# # # # for month_name in sorted(months.keys):
# # # #     print(month_name, end=' ')
# # # #tlds = {'Japan':'Tokyo', 'England':'London','Germany':'Berlin','France':'Paris'}
# # # #for country, tld in tlds.items():  
# # #  #   print(f"{country:20} | {tld}") 

# # # #for month_name in months.keys():
# # #     #print(month_name, end=' ')
# # # months = {'January':1,'February':2,'March':3}
# # # months_view = months.keys()
# # # #for key in months_view:
# # # months['December'] = 12
# # # #for key in months_view:
# # #     #print(key, end=' ')
# # # #print (list(months.items()))
# # # #print(months)
# # #    # print(key, end=' ')
# # # #for month_name in sorted(months.keys()):
# # #  #   print(month_name, end=' ')
# # # country_capitals1 = {'Belgium':'Brussels', 'Haiti':'Port-au-Prince'}
# # # country_capitals2 = {'Nepal':'Kathmandu','Uruguay':'Montevideo'}
# # # country_capitals3 = {'Haiti':'Port-au-Prince','Belgium':'Brussels'}
# # # print(country_capitals1 == country_capitals2 )
# # # print(country_capitals1 == country_capitals3) 
# # # print(country_capitals1 != country_capitals2)


    
# # #country_codes = {}
# # #country_codes.update({'South Africa':'za'})
# # #country_codes.update(Australia='ar')
# # #country_codes.update(Australia='au')
# # #print(country_codes)
# # #months = {'January':1,'February':2,'March':3}
# # #months2 = {number: name for name, number in months.items()}
# # #print(months2)
# # #grades = {'Sue':[98,87,94],'Bob':[84,95,91]}
# # #grades2 = {k:sum(v)/ len(v) for k, v in grades.items()}
# # #print(grades2)
# # print({number: number ** 3 for number in range(1, 6)})


# # Set
# #colors = {'red','orange','yellow','green','red','blue'}
# #print(colors)
# #print('purple' not in colors)
# #for color in colors:
#  #   print(color.upper(), end=' ')
# #numbers = list(range(10)) + list(range(5))
# #print(numbers)
# #print(set(numbers))
# #print(set())
# text = 'to be or not to be that is the question'
# unique_words = set(text.split())
# for word in sorted(unique_words):
#     print(word, end=' ')
#print({1,3,5} < {7,3,5,1})
#print({1,3,} <= {3,5,1})
#print({1,2}.issubset({3,5,1}))
#print({1,3,5} | {2,3,4})
#print({1,3,5}.union([20,20,3,40,40]))
#print({1,3,5} & {2,3,4})
#print({1,3,5}.intersection([1,2,2,3,3,4,4]))
#print({1,3,5} - {2,3,4})
#print({1,3,5,7}.difference([2,2,3,3,4,4]))
#print({1,3,5} ^ {2,3,4})
#print({1,3,5,7}.symmetric_difference([2,2,3,3,4,4]))
#print({1,3,5}.isdisjoint({2,4,6}))
#print({1,3,5}.isdisjoint({4,6,1}))

#Mutable mathematical set Operations
numbers = {1,3,5}
numbers |= {2,3,4}
numbers.update(range(10))
print(numbers)

#Methods for removing and adding Elements
#numbers.add(17)
#numbers.remove(3)
#numbers.clear()
#print(numbers)
numbers = [1,2,2,3,4,5,6,6,7,8,9,10,10]
evens = {item for item in numbers if item % 2 == 0}
print(evens)