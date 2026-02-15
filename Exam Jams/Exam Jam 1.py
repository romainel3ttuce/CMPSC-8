# 1st Question:

def digit(n, k):
    "Return the k-th digit from the right of n for positive integers n and k"
    return n // 10 ** (k) % 10

print(digit(3579, 2))

print(digit(3579, 0))

print(digit(3579, 10))

# 2nd Question:

def clamp(x: float, lo: float, hi: float):
    "Return x clamped to the inclusive range [lo, hi]"
    if x < lo:
        return lo
    if x > hi:
        return hi
    else:
        return x

print(clamp(5.0, 0.0, 10.0))

print(clamp(-2.0, 0.0, 10.0))

print(clamp(99.0, 0.0, 10.0))

# 3rd Question:

def max_of_pairs_mins(a: float, b: float, c: float, d: float, e: float, f: float):
    "Return the maximum of the minimums of the three pairs (a, b), (c,d), and (e, f)"
    min_a_b = min(a,b)
    min_c_d = min(c,d)
    min_e_f = min(e,f)
    return max(min_a_b, min_c_d, min_e_f)

print(max_of_pairs_mins(4.0, 3.7, 6.0, 3.5, 10.0, 9.0))

print(max_of_pairs_mins(1.0, 1.7, 4.5, 3.0, 2.2, 2.2))

print(max_of_pairs_mins(-5.0, -1.0, 0.0, 7.0, 3.0, 9.0))
