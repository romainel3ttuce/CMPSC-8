# Lecture 6 - Function Design + Docstring:

def is_even(value: int) -> bool:
    """
    Return True if and only if value is divisible by 2.

    >>> is_even(2)
    True
    >>> is_even(17)
    False
    """

    # returns true if the remainder is 0
    return value % 2 == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(is_even(17))

def total_slices(num_pizzas: int, slices_per_pizza: int) -> int:
    """
    Return the total number of slices in num_pizzas pizzas that each
    have slices_per_pizza slices.

    >>> total_slices(1, 8)
    8
    >>> total_slices(3, 12)
    36
    """

    # Calculating total number of pizza slices
    return num_pizzas * slices_per_pizza

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(total_slices(1,8))
