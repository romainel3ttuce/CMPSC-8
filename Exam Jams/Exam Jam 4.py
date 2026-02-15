# Question 1:

def get_different_matches(first):
    """Return a new list that contains each item in 1st that is not equal to the
    item immediately before it and not equal to the item immediately after it in 1st.
    The first and last items of 1st must not be included because they do not have
    items on both sides.
    Precondition: len(first) >= 3
    """
    
    matches = []

    # We use this range because we do not
    # want the first and last index to count
    # since they don't have a # before and
    # after respectively
    
    for i in range(1, len(first) - 1): 
        if first[i] != first[i + 1] and first[i] != first[i - 1]:
            matches.append(first[i])

    return matches

print(get_different_matches([1, 2, 3, 3, 4, 2]))
print(get_different_matches([2, 2, -1, 1, 6]))
print(get_different_matches([7, 7, 5, 5]))

# Question 2:

def is_balanced(s):
    """Returns True if s contains balanced parentheses."""
    
    open_paren = 0
    closed_paren = 0
    balanced = False

    for i in range(len(s)):
        if s[i] == "(":
            open_paren += 1
        else:
            closed_paren += 1

    return open_paren == closed_paren

print(is_balanced("(())()"))
print(is_balanced("(()"))

# Question 3:

# A TypeError occurs without the "range" in this code because i cannot be IN the
# length of nums, that would not make sense. Here, the rest of the code or the
# next line uses indexing, so we know that the for loop would not be for i in nums,
# since the next line would read total += i

nums = [1, 2, 3, 4]
total = 0

for i in range(len(nums)):
    total += nums[i]

print(total)

# The AttributeError occurs because append is a method that modifies the list
# in place and does not return the modified list itself. Before the code was
# 1st = 1st.append(1)

def add_one(lst):
    lst.append(1)
    return lst

a = [10, 20]
b = add_one(a)
print("a:", a)
print("b:", b)
