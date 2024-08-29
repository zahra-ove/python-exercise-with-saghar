# q1: extract prices of products by
# using for loop
# using map function
# using list comprehension

items = [
    ("product1", 10),
    ("product2", 120),
    ("product3", 53)
]




## ----- using for loop:

# prices = []
# for item in items:
#     prices.append(item[1])
    
# print(prices)

## ----- using map function (map function is a built-in function in python)
# items = [
#     ("product1", 10),
#     ("product2", 120),
#     ("product3", 53)
# ]
# prices = list(map(lambda item: item[1], items))
# print(prices)


## ----- list comprehension
# items = [
#     ("product1", 10),
#     ("product2", 120),
#     ("product3", 53)
# ]

# prices = [item[1] for item in items]
# print(prices)

#====================================================================================

# q2: return those products with  price greater than 50
# using filter function (which is built-in python function)
# using list comprehension


## ----- using filter function
items = [
    ("product1", 10),
    ("product2", 120),
    ("product3", 53)
]

filtered_items = list(filter(lambda item: item[1] > 50, items))
print(filtered_items)


## ----- list comprehension
items = [
    ("product1", 10),
    ("product2", 120),
    ("product3", 53)
]

filtered_items = [item[1] for item in items if item[1] > 50]
print(filtered_items)

#====================================================================================

# q3: combine given two lists to one list named list3.
list1 = [1,2,3]
list2 = [10,20,30]

result = list(zip(list1, list2))
print(result)

# and also we can pass any iterable to zip function.
result = list(zip("abc", list1, list2))
print(result)



#====================================================================================

# q4: how check if a list is empty?
# it is related to Falsy values in python.  -> 0, "", []

list1 = []
if list1:
    print("not empty")
else:
    print("empty")
    
# or better way:

if not list1:
    print("empty")
    
#====================================================================================

# q5: we have two variables x and y. swap the value of these two.
# given:  x=1,  y=2
# expected: x=2, y=1
x = 1
y = 2
# solution1
z = x
x = y
y = z

# solution2 -> using tuple unpacking
y, x = x, y

