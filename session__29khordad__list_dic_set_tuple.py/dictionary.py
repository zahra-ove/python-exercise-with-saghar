#dictionary
#------------------------------------------------
#1. Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# # empty dictionary
# res_dict = dict()

# for i in range(len(keys)):
#     res_dict.update({keys[i]: values[i]})
# print(res_dict)

# other solution:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
di = {}
for i in range(len(keys)):
    di[keys[i]] = values[i]
    
# print(di)

# exit(0)



#2. Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


#s1:
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = {**dict1, **dict2}
# print(dict3)


#s2:
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)



#3. Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }


#s:
# print(sampleDict['class']['student']['marks']['history'])


#4. Initialize dictionary with default values
# Given:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# Expected output: {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}


#hint: https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/dictionary/from-keys/python-dictionary-fromkeys/#:~:text=The%20Python%20fromkeys()%20built,value%20provided%20by%20the%20user.
#s:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# res = dict.fromkeys(employees, defaults)
# print(res)

# # Individual data
# print(res["Kelly"])

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result = {}

for emplyee in employees:
    # result[emplyee] = defaults
    # result.update({emplyee: defaults})
    
print(result)