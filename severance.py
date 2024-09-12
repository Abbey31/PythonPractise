# # # #Dictionary
# # # #counting in dict
# # # counts = dict()
# # # names = ['csev','cwen','csev','zqian','cwen']
# # # for name in names:
# # #     if name not in counts:
# # #         counts[name] = 1
# # #     else:
# # #         counts[name] = counts[name] + 1
# # # print(counts)
# # #get method with dictionary

# # counts = dict()
# # names = ['csev','cwen','zqian','cwen']
# # for name in names:
# #     counts[name] = counts.get(name, 0) + 1
# # print(counts)
# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
# for (k, v) in d.items():
#     print(k, v)
#     tups = d.items()
#     print(tups)
capitals = {'USA':'Washington DC',
            'India':'New delhi','China':'Beijing',
            'Russia':'Moscow'}
print(capitals.get('Germany'))
