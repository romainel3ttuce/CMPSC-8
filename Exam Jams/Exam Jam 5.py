# Exam Jam 5
# Question 1:

def seat_finder(n, l):
    count = 0
    indices = ""

    for i in range(len(l)):
        """Print the indices of a sequence of empty seats long enough to
        seat n people together.

        Seats are represented by the strings "empty" or "reserved".
        Search from left to right (starting at index 0).

        If no such sequence exists, print "No Seats".

        The function should NOT return anything.
        """
        if l[i] == "empty":
            count += 1
            indices += str(i) + " "
            if count == n:
                print(indices)
                # It is good practice to use return None if you want to leave 
                # a function and not return anything
                # If I get rid of this line and print the first call to seat_finder
                # it will print 0 1 (new line) No Seats (new line) None (as expected)
                return None 
            
        else:
            count = 0
            indices = ""
    print("No Seats")

print(seat_finder(2, ["empty", "empty", "reserved", "empty"]))
seat_finder(3, ["empty", "empty", "reserved", "empty"])
seat_finder(3, ["empty", "empty", "reserved", "empty", "empty"])

# Question 2:

"""
def add_lengths(words):
    lengths = []
    for w in words:
        lengths.append(w)
    for x in lengths:
        x += len(x)
    return lengths

The error occurs on line 6, because you cannot concatenate strings to ints
without casting.
"""

# Question 3:

a = 18
b = 24

while b != 0:
    a, b = b, a % b

print(a)
