
# # roman_numerals = {'I':1, 'II':2,'III':3,'V':5,'X':100}
# # roman_numerals['L'] = 50
# # res = roman_numerals.get("I")
# # print(roman_numerals)
# # print(res)
# months = {'January':1,'February':2,'March':3}
# #for month_name in months.keys():
#     #print(month_name, end=' ')
# #for month_name in months.values():
#  #   print(month_name, end=' ')
# months_view = months.keys()
# for key in months_view:
#     print(key, end=' ')
# months['December'] = 12
# print(months)
# #for key in months_view:
# #    print(key, end=" ")
# #print(list(months.values()))
# for month_name in sorted(months.keys):
#     print(month_name, end=' ')
tlds = {'Japan':'Tokyo', 'England':'London','Germany':'Berlin','France':'Paris'}
for country, tld in tlds.items():  
    print(f"{country:20} | {tld}")  