# Handout 10:

# Question 1:
def add_student(students: list, student_id: int, name: str, gpa: float) -> None:
    """students is a list of student records. Each record must be stored as a
    tuple in the form (student_id, name, gpa).
    Your function must create the tuple using the given values, append it
    to students, and not return anything.
    You may assume the list already exists and is passed into the function.

    >>> students = [(100, "Bob", 3.5)]
    >>> add_student(students, 101, "Alice", 3.8)
    >>> print(students)
    [(100, "Bob", 3.5), (101, "Alice", 3.8)]
    """
    values = (student_id, name, gpa)
    students.append(values)

students = [(100, "Bob", 3.5)]
add_student(students, 101, "Alice", 3.8)
print(students)

# Question 2:
from typing import List

def stretch_string(s: str, stretch_factors: List[int]) -> str:
    """Return a string consisting of the characters in s in the same order
    as in s, repeated the number of times indicated by the item at the
    corresponding position of stretch_factors.

    Precondition: len(s) == len(stretch_factors) and the values in
                  stretch_factors are non-negative

    >>> stretch_string('Hello', [2, 0, 3, 1, 1])
    'HHllllo'
    >>> stretch_string('echo', [0, 0, 1, 5])
    'hooooo'
    """
    new_string = ""

    for i in range(len(s)):
        new_string = new_string + s[i] * stretch_factors[i]

    return new_string

print(stretch_string('Hello', [2, 0, 3, 1, 1]))
print(stretch_string('echo', [0, 0, 1, 5]))

# Question 3:
def greatest_difference(nums1: List[int], nums2: List[int]) -> int:
    """Return the greatest absolute difference between numbers at corresponding
    positions in nums1 and nums2.

    Precondition: len(nums1) == len(nums2) and nums != []

    >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    >>> greatest_difference([1, -2, 3], [-6, 8, 10])
    7
    """
    max_difference = 0
    
    for i in range(len(nums1)):
        
        difference = abs(nums1[i] - nums2[i])

        if difference > max_difference:
            max_difference = difference

    return max_difference

print(greatest_difference([1, 2, 3], [6, 8, 10]))
print(greatest_difference([1, -2, 1], [-6, 8, 1]))
