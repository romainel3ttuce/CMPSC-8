# Lecture 10 - Function Calls:

def func1(a, b):
    y = x + a # Global variables aren't a common practice + shouldn't be used
    # that much unless you're using a constant in your code like pi, arguments
    # make your code more efficient in readability
    return y + b

x = 1
y = 2
z = 3 
z = func1(4, 5)
print(x, y, z)

def func1(x ,y):
    return x + y
def func2(x, y):
    return x * y
def func3(x, y):
    return(func1(x, y) - func2(1, y))
def main():
    print(func3(1, 2))
main()

def numbers(a, b):
    counter = 1
    while a != b:
        print(counter)
        counter += 1
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(numbers(12, 15))

# Tuples:

student = ('Marc', 123456789, 9.5)
print(student)
print(student[1])
# student[2] = 10 --> this line gives an error because tuples are an immutable
# collection of values

emptyTuple = ()

names = (x,) # defines a tuple containing 1 value

def foo():
    return x, y

print(type(foo()))

t = 1, 2
print(t[0])
print(t[1])
a, b = t
print(a)
