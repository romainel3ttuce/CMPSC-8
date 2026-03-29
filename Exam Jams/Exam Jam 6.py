# Exam Jam 6
# Question 1:

def invert_dict(dict):
    """
    Return a new dictionary where keys and values are swapped.

    You may assume all values in d are unique
    """
    new_dict = {}

    for element in dict:
        new_dict[dict[element]] = element
        
    return new_dict

print(invert_dict({'a':1, 'b':2}))

# Question 2:

def count_frequencies(words):
    """
     Return a dictionary mapping each word in words to the number of times
     it appears.
     """
    map = {}
    count = 1
    
    for element in words:
        if element not in map:
            map[element] = 1
        else:
            map[element] += 1
            
    return map

print(count_frequencies(["a", "b", "a", "c", "b", "a"]))

# Question 3:

def first_repeats(s):
    """
    Returns the first character in s that appears more than once.
    """
    repeats = set()

    for element in s:
        if element not in repeats:
            repeats.add(element)
        else:
            return element
            
    return ''

print(first_repeats("swiss"))
print(first_repeats("abc"))
