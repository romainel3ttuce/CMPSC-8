# Handout 06:

# Question 1:
wish = 'Happy Birthday'

print(wish[0].lower() + wish[6].lower())
print(wish.swapcase())
print(wish[0].lower() + wish[1:6].lower() + wish[6].lower() + wish[7:])
print(wish.lower())

# Question 2:
robot = 'R2D2'
robot2 = 'R2D2$'

print(robot.isupper())
print(robot.isalpha())
print(robot.isalnum())
print(robot.isdigit())
print(robot.islower())

# My own test
print(robot2.isupper())
print(robot2.isalpha())
print(robot2.isalnum())
print(robot2.isdigit())
print(robot2.islower())

# Question 3:
def count_uppercase(s: str) -> int:
    """Return the number of uppercase letters in s.

    >>> count_uppercase('Romina')
    1
    """
    count = 0
    for i in range(len(s)):
        if s[i] == s[i].upper():
            count += 1
            
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Question 4:
def add_underscores(s: str) -> str:
    """Return a string that contains the characters from s with an underscore
    added after every character except the last.

    >>> add_underscores('hello')
    'h_e_l_l_o'
    """
    new_string = ""
    for i in range(len(s)):
        if i == len(s) - 1:
            new_string = new_string + s[i]
        else:
            new_string = new_string + s[i] + "_"

    return new_string

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Question 5:
def every_nth_character(s: str, n: int) -> str:
    """Return a string that contains every nth character from s, starting at
    index 0.

    Precondition: n > 0

    >>> every_nth_character('Computer Science', 3)
    'CpeSee'
    """
    result = ''
    i = 0 # The index of the next character to examine.

    while i < len(s):
        result = result + s[i]
        i = i + n

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
