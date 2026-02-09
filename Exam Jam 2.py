# Question 1.

def count_collatz_steps(n):
    count = 0
    while(n != 1):
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        count += 1
    return count

n = int(input())
print(count_collatz_steps(n))

# Question 2.

def itvFib(n):
    old = 0
    new = 1
    for i in range(n):
        fib_num = old + new
        old = new
        new = fib_num
    return fib_num

print(itvFib(5))
print(itvFib(4))
print(itvFib(3))

