# Lecture 7: Strings:

foo = "hello"
print(id(foo[0]))

greeting = 'Hello, world!'
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)

print("Hello World!" == 'Hello World!')
myStr1 = "Maryam's Lecture ROCKS!"
myStr2 = 'The students agreed: "Yes, it does!"'
myStr3 = '''hello
            my name is Maryam'''
print(myStr3)

Course = "CMPSC 8"
m = Course[2]
print(m)
lastchar = Course[-1]
print(lastchar)

print('John' 'Smith' 'Hi')
print('John', 'Smith')
print('John' + 'Smith')

name = input("What's your name?")

print(f"Hello {name}!")

print("Hello {0}!".format(name))

print("Hello %s!" %(name))

name = "Maryam"
yearlyPaidTax = 32945.22
print(f'{name:<10} pays {yearlyPaidTax:>10} every year.')

width = 10
precision = 5
someValue = 12.12345
print(f"someValue = {someValue:{width}.{precision}}")

print(f"someValue = {someValue:12.5f}")

print("Go" * 6)
name = "Travelers"
print(name * 3)
print(name + "Go" * 3)
print((name + "Go") * 3)

ss = "Hello, World!"
print(ss.upper())
print(ss.lower())

els = ss.count("1")
print(els)
print("***" + ss.strip() + "***")
print("***" + ss.lstrip() + "***")
print("***" + ss.rstrip() + "***")
news = ss.replace("o", "***")
print(news)

person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)

singers = 'Peter, Paul, and Mary'
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])

a = "this is a string"
# a = a.split("a")
print(a)

for word in a.split(" "):
    print(word)

fruit = "Banana"
sz = len(fruit)
last = fruit[sz - 1]
print(last)
