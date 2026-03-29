# Lecture #12 (2/23/26):

# Creating a Dictionary:
students = {123:'Alice', 124:'Bob', 125:'Charles'}

# Adding Elements to Dictionary:
myDictionary = {}

'''
This is how you add to the dictionary, because 123 (the key) does not exist,
in the dictionary, the key and corresponding value are added to the dictionary!
'''
myDictionary[123] = 'Alice'
myDictionary[124] = 'Bob'
myDictionary[125] = 'Alice'
print(myDictionary)
myDictionary[123] = 'Charles'
print(myDictionary)

# Make empty dictionary
students = {}
print(f'students = {students}')

# Make an initially filled dictionary
students = {101:'Ken', 102:'Tony', 100:'Marc'}
print(f'students = {students}')

# Get size
print(f'size = {len(students)}')

# Add items to dictionary
students[103] = 'Maryam'
print(f'students = {students}')

# Update item in dictionary
students[101] = 'Jim'
print(f'students = {students}')

# Remove key and value
del students[102]
print(f'students = {students}')

# Pop key and return value
print(students.pop(103))
print(f'students = {students}')

# Print keys (unsorted)
print(f'keys = {list(students.keys())}')

# Print values (unsorted)
print(f'values = {list(students.values())}')

# Print item tuples (key, value) (unsorted)
print(f'items = {list(students.items())}')

# Get an item by key
num = int(input('Please enter an item number to search: '))
if (num in students):
    print("Found the item", students[num])
else:
    print("Not found")

# Sort the keys
print(f'sorted = {sorted(students.keys())}')

# Empty dictionary
students.clear()
print(f'cleared dicts = {students}')


