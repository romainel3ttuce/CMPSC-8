# Handout 09:

a = 5
b = 4
c = 6

print(id(a))
print(id(b))
print(id(c))

a = 5

print(id(a))

a = 3
b = a

print(id(a))
print(id(b))

a = 5

print(id(a))

b = a + 2

print(id(b))

a = 10

print(id(a))

# Question 1:

a = [0, 1, 2]
b = a
b[2] = 100

# After the code above is executed, which of the following expressions
# evaluate to True?

print(a == [0, 1, 2] and b == [0, 1, 100])
print(a == [0, 1, 2] and b == [0, 100, 2])
print(a == [0, 1, 100] and b == [0, 1, 100])
print(id(a) == id(b))

# Question 2:

a = [1, 0]

# All of the following code fragments cause a to refer to [1, 0, 8]
# Which code fragments create a new list?
# Which code fragments modify the original list?

a.append(8)
a.insert(len(a), 8)
a = a + [8]
a = [a[0], a[1], 8]

# Question 3:

a = [1, 0, 8]
b = a.sort()

# After the code above is executed, which of the following expressions evaluate
# True?

print(a == [1, 0, 8])
print(a == [0, 1, 8])
print(b == [1, 0, 8])
print(b == [0, 1, 8])

print(id(a))
print(b)
