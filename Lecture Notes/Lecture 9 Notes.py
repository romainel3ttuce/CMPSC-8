# Lecture #9: Lists:

names = ['Marc', 'Ken', 'Jim', 'Tony']

print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(names)
print(len(names))
print(names.index('Ken'))

stuff = [1, "CMPSC", 3.14]
for item in stuff:
    print(item)

for i in range(0, len(stuff)):
    print(stuff[i])

print(names[:])
print(names[0:2])
print(names[-2:1])

print(names[0:len(names):1])
print(names[::])
print(names[::-1])
print(names[-2::])
print(names[::2])

names[1] = "Johnathan"
print(names)

names = names + ['Jack']
names.append('Daniel')
names.insert(3, 'Chris')
names.extend(['Eric', 'Frank'])

print(names)

names = []
name = input("Enter a name:")
names.append(name)
names_str = input("Enter names seperated by comma:")
names.extend(names_str.strip().split(","))
print(names)

print(f'names = {names}')

for i in range(0, len(names), 1):
    print(f'names[{i}] = {names[i]}')

names = ['Marc', 'Ken', 'Jim', 'Tony']
new_names = names
new_names[0] = "Maryam"
print(names[0])

new_names = names[:]
new_names = names * 1
new_names = []
new_names.extend(names)

new_names = []
for i in range(0, len(names), 1):
    new_names.append(names[i])

print(names)

data = [11, 12, 13, 14]
print(data.index(12))

x = [1, 2, 1, 3, 4, 2, 1]
x.remove(1)
print(x)

x = 2
myList = [1, 2, 1, 3, 4, 2, 1]

while x in myList:
    myList.remove(x)

print(myList)

myList = [1, 2, 3, 4]

myList.pop()
print(myList)

myList.pop(0)
print(myList)

myList.pop(myList.index(2))
print(myList)
