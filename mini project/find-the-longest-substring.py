### Find the Longest Substring Without Repeating Characters ###
# Given a string, find the length of the longest substring without repeating characters.
# Example
# Input: "abcabcbb"
# Output: 3 ("abc" is the longest substring)

# Input: "bbbbb"
# Output: 1 ("b" is the longest substring)

# Input: "pwwkew"
# Output: 3 ("wke" is the longest substring)







def max_nonrepeat_string(str):
    nonrepeat_Strings = []
    test = []
    
    for char in str:
       if char not in test:
         test.append(char)   
       else:
           nonrepeat_Strings.append(''.join(test))
           test.clear()
           test.append(char)
           
    nonrepeat_Strings = list(set(nonrepeat_Strings))
    longest_string = max(nonrepeat_Strings, key=len)
    print(longest_string)
    
    
    
max_nonrepeat_string("abcabcbb")
quit()    
















def length_of_longest_substring(s):
    char_index_map = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        
        char_index_map[char] = i

    return max_length

# Test cases
print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))     # Output: 1
print(length_of_longest_substring("pwwkew"))    # Output: 3




def max_none_repeatable_string(target):
    acc = []
    lists = []
    for char in target:
        if char not in acc:
            acc.append(char)
        else:
            res = " ".join([str(item) for item in acc])
            lists.append(res)
            acc = []
    
    print(lists)
    quit()
    
    lists_stat = {}
    for i in lists:
        lists_stat[i] = len(lists[i])
    
    max_length = max(lists_stat.values())
    return [key for key, value in lists.items() if value == max_length]
        
print(max_none_repeatable_string("abcvfgd"))
