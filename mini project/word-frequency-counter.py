### Word Frequency Counter ###
# Given a string, count the frequency of each word 
# in the string and return a dictionary with the words as keys and their frequencies as values.

# Example:
# Input: "this is a test this is only a test"
# Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}



def word_frequency(s):
    words = s.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Test case
print(word_frequency("this is a test this is only a test"))
