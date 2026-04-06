# Handout 08:

def can_pay_with_two_coins(denoms: list[int], amount: int) -> bool:
    """Return True if and only if it is possible to form amount, which is a
    number of cents, using exactly two coins. The two coins can be of any of
    the denominations in denoms.

    >> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 20)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    False
    """
    num_coins = 0

    denoms.sort()
    denoms.reverse()

    for i in range(len(denoms)):
        while amount >= denoms[i]:
            num_coins += 1
            amount -= denoms[i]

    if num_coins == 2:
        return True

    return False

print(can_pay_with_two_coins([1, 5, 10, 25], 35))
print(can_pay_with_two_coins([1, 5, 10, 25], 20))
print(can_pay_with_two_coins([1, 5, 10, 25], 12))

def scale_midterm_grades(grades: list[int], multiplier: int, bonus: int) -> None:
    """Modify each grade in grades by multiplying it by multiplier and then
    adding bonus. Cap grades at 100.

    >>> grades = [45, 50, 55, 95]
    >>> scale_midterm_grades(grades, 1, 10)
    >>> grades
    [55, 60, 65, 100]
    """
    for i in range(len(grades)):
        if grades[i] != 100:
            bonus_points = multiplier * bonus
            grades[i] += bonus_points
            if grades[i] > 100:
                grades[i] = 100
                
grades = [45, 50, 55, 95]
scale_midterm_grades(grades, 1, 10)
print(grades)

def collect_below_threshold(nums: list[int], threshold: int) -> list[int]:
    """Return a new list consisting of those numbers in nums
    that are below threshold, in the same order as in nums.

    >>> collect_below_threshold([1, 2, 3, 4], 3)
    [1, 2]
    >>> collect_below_threshold([1, 2, 108, 3, 4], 50)
    [1, 2, 3, 4]
    >>> collect_below_threshold([], 7)
    []
    """
    new_list = []

    for num in nums:
        if num < threshold:
            new_list.append(num)

    return new_list

print(collect_below_threshold([1, 2, 3, 4], 3))
print(collect_below_threshold([1, 2, 108, 3, 4], 50))
print(collect_below_threshold([], 7))

t = 1, 2
print(t[0])
print(t[1])
a, b = t
print(a)
