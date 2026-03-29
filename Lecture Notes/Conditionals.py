# Lecture #5: Conditionals:

x = 1.0
y = 2.0
c = (x <= y)
print(type(c))

a = 3
b = (a != 3)
print(b)

x = -2
y = 5
z = 0
print(x < y and z)

age = int(input("What is your age?"))

if age <= 17:
    print('You are underage!')

grade = int(input("Enter a grade value"))
letter_grade = ""

if grade >= 50:
    letter_grade = 'P'
    print('You pass!')
else:
    letter_grade = 'F'
    print('Try Harder!')

print('Thank You!')

x = int(input("Enter an integer value for x: "))
y = int(input("Enter an integer value for y: "))

if x < y:
     print("x is smaller than y.")
elif x > y:
     print("x is larger than y")
else:
    print("x and y are equal.")

# Incorrect results
grade = 97

if (grade >= 95):
    letterGrade = 'A+'
if (grade >= 90):
    letterGrade = 'A'
if (grade >= 85):
    letterGrade = 'A-'
if (grade >= 80):
    letterGrade = 'B+'

print(letterGrade)

# Correct results
grade = 97

if (grade >= 95):
    letterGrade = 'A+'
elif (grade >= 90):
    letterGrade = 'A'
elif (grade >= 85):
    letterGrade = 'A-'
elif (grade >= 80):
    letterGrade = 'B+'

print(letterGrade)

def fizzbuzz():
    num = 1
    exit_func = False
    
    while exit_func != True:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
            
        exit_input = input("Do you want to exit?")

        if exit_input == 'yes':
            exit_func = True
        num += 1

print(fizzbuzz())
