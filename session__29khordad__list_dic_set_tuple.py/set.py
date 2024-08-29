# Given a list of lists, find the common elements across all lists. Use sets to solve this problem efficiently.
# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 6, 7]
list3 = [3, 4, 5, 8, 9]

#s1
# common_elements = set(list1) & set(list2) & set(list3)
# print(common_elements)

#s2

# def find_common_elements(*args):
#     common_items = set(args[0])
#     for item in args:
#         common_items &= set(item)
    
#     return common_items

# print(find_common_elements(list1,list2,list3))