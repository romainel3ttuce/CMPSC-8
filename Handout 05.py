# Handout 05:

# Question 1:
def earlier_name(name1: str, name2: str) -> str:
    """Return the name, name1 or name2, that comes first alphabetically

    >>> earlier_name('Jen', 'Paul')
    'Jen'
    >>> earlier_name('Colin', 'Colin')
    'Colin'
    """
    # Checks if name1 is greater than name2:
    if name1 < name2:
        return name1
    return name2

if __name__ == "__main__":
    import doctest
    doctest.testmod()

def ticket_price(age: int) -> float:
    """Return the ticket price for a person who is age years old.
    Seniors 65 and over pay 4.75, kids 12 and under pay 4.25 and
    everyone else pays 7.50.

    Precondition: age > 0

    >>> ticket_price(7)
    4.25
    >>> ticket_price(21)
    7.5
    >>> ticket_price(101)
    4.75
    """
    # Checks age of individuals and returns corresponding ticket price
    if age >= 65:
        return 4.75
    elif age <= 12:
        return 4.25
    return 7.50

if __name__ == "__main__":
    import doctest
    doctest.testmod()

def is_teenager(age: int) -> bool:
    """Return True if and only if age is a teenager between 13 and 18 inclusive.

    >>> is_teenager(4)
    False
    >>> is_teenager(16)
    True
    >>> is_teenager(19)
    False
    """
    # Returns whether the age inputted is between 13 and 18 inclusive
    return age >= 13 and age <= 18

if __name__ == "__main__":
    import doctest
    doctest.testmod()
