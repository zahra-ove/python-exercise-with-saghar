#list
#------------------------------------------------
#1. How do you flatten a nested list?
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# flatten_list = []
# for outer_item in nested_list:
#     for i in outer_item:
#         flatten_list.append(i)
        
# print(flatten_list)
        
# flattened_list = [item for sublist in nested_list for item in sublist]
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


#2. How do you merge two sorted lists into a single sorted list?
# list1 = [1, 3, 5]
# list2 = [2, 4, 6]

# merges_list = sorted(list1 + list2)
# # merges_list.sort()
# print(merges_list)








# merged_list = sorted(list1 + list2)
# print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]





#3. How do you reverse a list in Python?
#S1:
# my_list = [1, 2, 3, 4, 5]





# my_list.reverse()
# print(my_list)  # Output: [5, 4, 3, 2, 1]

#S2:
# reversed_list = my_list[::-1]
# print(reversed_list)  # Output: [5, 4, 3, 2, 1]



#4. How do you rotate a list by n positions?
# def rotate_list(lst, n):
#     # n = n % len(lst)  # Handle rotation greater than list length
#     return lst[-n:] + lst[:-n]


# my_list = [1, 2, 3, 4, 5]



# rotated_list = rotate_list(my_list, 2)
# print(rotated_list)  # Output: [4, 5, 1, 2, 3]




# #5. How do you find the index of an element in a list?
# my_list = [1, 2, 3, 4, 5]
# print(my_list.index(5))







# index_of_3 = my_list.index(3)
# print(index_of_3)  # Output: 2


#6. How do you remove duplicates from a list?
# my_list = [1, 2, 2, 3, 4, 4, 5]
# # unique_list = list(set(my_list))
# unique_list = list(set(my_list))
# print(unique_list)

# init_list = []
# for i in my_list:
#     if i not in init_list:
#         init_list.append(i)

# print(init_list)







# print(unique_list)  # Output: [1, 2, 3, 4, 5]


#7. How do you find the maximum value in a list?
my_list = [1, 2, 3, 4, 5]
x = max(my_list)
print(x)






# max_value = max(my_list)
# print(max_value)  # Output: 5




#8. How do you get the sum of all elements in a list?
# my_list = [1, 2, 3, 4, 5]
# total = sum(my_list)
# print(total)  # Output: 15


#9. How do you create a list of the first 10 natural numbers?
# natural_numbers = list(range(1, 11))
# print(natural_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#10. How do you check if a list is empty?
#s1:
# my_list = []
# is_empty = len(my_list) == 0
# print(is_empty)  # Output: True

#s2:
# is_empty = not my_list
# print(is_empty)  # Output: True

#11. How do you make a shallow copy of a list?
# my_list = [1, 2, 3, 4, 5]
# shallow_copy = my_list.copy()
# print(shallow_copy)  # Output: [1, 2, 3, 4, 5]


#12. How do you concatenate a list of strings into a single string with spaces?
# string_list = ["hello", "world"]
# single_string = " ".join(string_list)
# print(single_string)  # Output: "hello world"


#13. How do you find the second largest element in a list?
# my_list = [1, 3, 4, 5, 0, 2]
# unique_list = list(set(my_list))  # Remove duplicates
# unique_list.sort()
# second_largest = unique_list[-2]
# print(second_largest)  # Output: 4


#14. How do you find all the even numbers in a list?
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# even_numbers = [num for num in my_list if num % 2 == 0]
# print(even_numbers)  # Output: [2, 4, 6, 8]


#***15. How do you transpose a 2D matrix represented as a list of lists?
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transposed_matrix)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


#16. How do you find the common elements in three lists?
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# list3 = [5, 6, 7, 8, 9]
# common_elements = list(set(list1) & set(list2) & set(list3))
# print(common_elements)  # Output: [5]


#17. How do you remove all occurrences of a specific element from a list?
# my_list = [1, 2, 3, 2, 4, 2, 5]
# element_to_remove = 2
# filtered_list = [elem for elem in my_list if elem != element_to_remove]
# print(filtered_list)  # Output: [1, 3, 4, 5]

#18. How do you group elements of a list based on a specific condition (e.g., odd and even)?
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = [num for num in my_list if num % 2 != 0]
# even_numbers = [num for num in my_list if num % 2 == 0]
# print("Odd numbers:", odd_numbers)  # Output: Odd numbers: [1, 3, 5, 7]
# print("Even numbers:", even_numbers)  # Output: Even numbers: [2, 4, 6, 8]