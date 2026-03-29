# Lecture 8: Loops:

total = 0
num = int(input('Please enter number of iterations'))
for i in range(1, num + 1, 1):
    total = total + i
    print(total)

userinput = int(input('Please enter number of iterations'))
total = 0
while userinput != 0:
    total = total + userinput
    userinput = int(input('Plz enter a number, \'0\' to end'))

sum = 0

for i in range(0, 101, 1):
    sum = sum + i
    
print(sum)

sum = 0
i = 0

while i < 101:
    sum = sum + i
    i = i + 1

print(sum)

for i in range(1, 3, 1):
    for j in range(1, 4, 1):
        print('i = %d, j = %d' %(i, j))
    print('---------------------')

for i in range(5, 0, 2):
    print('i = %d' % (i))
    
