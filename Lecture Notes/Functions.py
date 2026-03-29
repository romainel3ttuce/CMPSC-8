# Lecture 3: Functions:
# Minimal function that doesn't do anything.
def foo():
    pass

# My own function!
def dbl(x):
    """
    Returns double its input, x
    """
    return 2 * x

def pay(amount):
    print("Direct bank deposit: $%d." %(amount))

# Calculate payroll
salary = 40 * 15
pay(salary)

def printbar(char, num):
    bar = ''
    for i in range(1, num + 1, 1):
        bar = bar + char
    print(bar)

printbar('-', 3)
length = 10
printbar('=', length)

# The following calls to the printbar function do not work.
# printbar('-')
# printbar(3)
# printbar(length)
# printbar(3, '-')

def printbar(char, num = 10):
    bar = ''
    for i in range(num + 1):
        bar = bar + char
    print(bar)

printbar('-')
printbar('=', 20)

def foo(x = 1, y = 2):
    print("x =", x, "y =", y)

foo()
foo(3)
foo(3,4)


# A function in python always returns something.
def foo():
    return None

print(foo())

def foo():
    pass
print(foo())

def earlier_name(name1, name2):
    """Return the name, name1 or name2, that comes first alphabetically.
    >>> earlier_name('Jen', 'Paul')
    'Jen'
    >>> earlier_name('Colin', 'Colin')
    'Colin'
    """
    if name1 < name2:
        return name1
    return name2

result1 = earlier_name('Jen', 'Paul')
result2 = earlier_name('Colin', 'Colin')
print(result1)
print(result2)

"""
Functions must be declared before calling. This will give a NameError:

print(foo())

def foo():
    return None
"""

def payroll(rate, hours):
    bonus = 5
    salary = rate * (hours + bonus)
    return salary

payment = payroll(hours = 40, rate = 15)
print("$%d has been paid." % payment)

def add(x, y):
    return x + y

result = add(5, 7)
print(f"add(5,7) is {result}")

result = add('Tora', 'Bora')
print(f"add('Tora', 'Bora') is {result}")

def add(x, y):
    return (x + y)

result = add('Tora', 'Bora')
print(f"add('Tora', 'Bora') is {result}")
