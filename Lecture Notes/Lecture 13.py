# Lecture 13 (2/25/26): Set:

# Creating a set
names = {"Albert", "Brian", "Carl"}

nums = {10.0, 9.0, 8.5, 5.0, 7.5}
letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
names = {'Marc', 'Jim', 'Ken'}
mixed = {1.0, 1, 'this', True}

names = set()

a = [5, 4, 3, 2, 1]
b = [6, 2, 4, 3, 3]

set_sub = set()
for num1 in a:
    for num2 in b:
        set_sub.add(num1 - num2)


print(set_sub)

A = {1, 2, 3}
B = {2, 6, 7}

print(A.intersection(B))

print(A.union(B))

print(A.symmetric_difference(B))

print(B.difference(A))

print(A.isdisjoint(B))

print(A.issubset(B))

print(A.issuperset(B))

print(A == B)

print(A != B)

print(A < B)

print(A > B)

# Files:

info = input("Please enter the info")

import os

print("exist?", os.path.exists("small network data.txt"))

from typing import TextIO:

def is_correct(file: TextIO, word: str)
