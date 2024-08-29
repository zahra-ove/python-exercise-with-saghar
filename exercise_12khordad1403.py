# Q1 
# Write a function that takes a string and 
# returns a dictionary with the count of each character in the string.


# solution
# def count_characters(s):
#     char_count = {}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     return char_count

# # Example usage:
# print(count_characters("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

#------------------------------------------------------------------------------------------


# Q2
# Write a function that takes a list of integers and 
# returns the sum of all even numbers in the list.


# solution
# def sum_even_numbers(numbers):
#     return sum(num for num in numbers if num % 2 == 0)

# # Example usage:
# print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: 12

#------------------------------------------------------------------------------------------


# Q3
# Write a function that takes two lists and 
# returns a list containing only the elements that are common to both lists.


def find_common_elements(list1, list2):
    
    common_elements = [];
    
    for e1 in list1:
        if e1 in list2:
            common_elements.append(e1)
            
    
    print(common_elements)
    
    
find_common_elements([1,2,3,4,7], [8,9,0,7,1])


# solution
# def common_elements(list1, list2):
#     return [element for element in list1 if element in list2]

# # Example usage:
# print(common_elements([1, 2, 3], [3, 4, 5]))  # Output: [3]

#------------------------------------------------------------------------------------------


# Q4
# Write a function that takes a string and 
# returns True if it is a palindrome (reads the same forwards and backwards), 
# and False otherwise.


# solution
# def is_palindrome(s):
#     return s == s[::-1]

# # Example usage:
# print(is_palindrome("radar"))  # Output: True
# print(is_palindrome("python"))  # Output: False
