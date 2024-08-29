### Pascal’s Triangle ###
# Write a function that generates the first n rows of Pascal’s triangle.

# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1, 1],
#    [1, 2, 1],
#   [1, 3, 3, 1],
#  [1, 4, 6, 4, 1]
# ]


list = [1, 1]
n = 4 #input('number of rows:\n')
c = 0

print('[1]')
print('[1,1]')
    
while c < n:
    c+=1
    list_length = int(len(list))
    iterate_limit = list_length - 1
    new_row = [1]
    for i in range(iterate_limit):
        new_elem = list[i] + list[i+1]    
        new_row.append(new_elem)
    
    new_row.append(1)
    print(new_row)
    list = new_row