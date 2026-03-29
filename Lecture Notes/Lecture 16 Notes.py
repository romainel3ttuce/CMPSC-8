# Lecture 16 (3/9/26): Recursion:

def factorial(n):
    if n == 0: # BASE CASE
        return 1
    return n * factorial(n - 1) # RECURSIVE CASE

print(factorial(3))

