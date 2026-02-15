# Question 1:

seats = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]

def empty_seats(seats):
    """Return the longest consecutive chain of empty seats (0) in seats."""
    maximum = 0
    current = 0
    new_current = 0
    for i in range(len(seats)):
        if seats[i] == 0:
            current += 1
        if seats[i] == 1 or i == (len(seats)-1):
            new_current = current
            current = 0
        if new_current > maximum:
            maximum = new_current
            new_current = 0
    return maximum

print(empty_seats(seats))

# Question 2:

def has_letter_case(s):
    """Return True if and only if s contains at least one lowercase letter
    and at least one uppercase letter."""
    is_lower = False
    is_upper = False
    for i in range(len(s)):
        if s[i].islower():
            is_lower = True
        if s[i].isupper():
            is_upper = True
    return is_lower and is_upper

print(has_letter_case('abcDEF'))
print(has_letter_case('abc123'))
print(has_letter_case('ABCXYZ'))

# Question 3:

def char_count(s, words):
    """Return a new list in which each item is the number of times
    that the character at the corresponding position of s appears
    in the string at the corresponding position of words. Lowercase
    and uppercase characters are considered different."""
    new_string = []
    for i in range(len(words)):
        word = words[i]
        letter = s[i]
        count = 0
        for let in word:
            if let == letter:
                count += 1
        new_string.append(count)
    return new_string

s = 'anb'
words = ['apple', 'banana', 'orange']

print(char_count(s, words))

s = 'xdaao'
words = ['cat', 'dog', 'cat', 'banana', 'cool']

print(char_count(s, words))

s = 'fW'
words = ['sanwiches', 'waffles']

print(char_count(s, words))
