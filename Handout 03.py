# Handout 03: Built-in Functions:

print(round(1.6))
print(round(3.14159, 2))
print(round(1234.5678, -2))
print(round(2.5))

x = 4
y = 5
x = 2

print(x)
print(y)

x = 4
y = x + 2
x = y + 1

print(x)
print(y)

def double(num):
    """Return twice the value of num.

    >>> double(7.0)
    14.0
    >>> double(5.7)
    11.4
    """
    return num * 2

print(double(7.0))
print(double(5.7))

def our_maximum(num1, num2):
    """Return the larger of num1 and num2.

    >>> our_maximum(1.5, 2.5)
    2.5
    >>> our_maximum(4.0, 3.7)
    4.0
    """
    return max(num1, num2)

print(our_maximum(1.5, 2.5))
print(our_maximum(4.0, 3.7))

def max_of_min(num1, num2, value1, value2):
    """Return the maximum of the minimum of the pairs num1 and num2,
    and value1 and value2.

    >>> max_of_min(5.0, 7.0, 3.0, 1.0)
    5.0
    >>> max_of_min(7.0, 3.2, 6.7, 6.9)
    6.7
    """
    min1 = min(num1, num2)
    min2 = min(value1, value2)
    return max(min1, min2)

print(max_of_min(5.0, 7.0, 3.0, 1.0))
print(max_of_min(7.0, 3.2, 6.7, 6.9))
