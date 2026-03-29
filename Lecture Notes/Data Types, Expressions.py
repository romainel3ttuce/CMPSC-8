# Lecture 2 - Data Types, Expressions:

print('Hello' + 'World')
print('Hello ' + 'World')
print('Yuh' + 'o' * 5 + '!')

print('2' + '2')

print(type(4.2))
print(type(True ))
print(type(4))
print(type("Flying Circus"))
print(type("42"))

print(int(4.2))
print(float(True))
print(float(4) / 5)
print(str(42))
print(int("42"))

print(type("Hello, World"))
print(type(17))
print(type(3.14))

a = 2
b = 3.14
c = "Hello World!"

a = a * a
b = b * b

print(a)
print(b)
print(c * 2)

print("spam spam spam spam spam spam baked beans spam spam spam" == "spam " * 6 + "baked beans " + "spam " * 2 + "spam")

x = 42
y = x
x == 101
print(x)
print(y)

x = 41
y = x + 1
print(x)
print(y)
x = x + y
print(x)
print(y)

user_name = input("Enter your name: ")
print("Hello", user_name, "!")
print(type(user_name))

"""
A program to calculate the time it takes to travel a given distance with a given
speed.
"""
distance = float(input())
speed = float(input())
time = distance / speed
print(f"Travel time: {time}")
