import math
def f(x):
    return x**2 - 4


def check_complexity(a, b, e):
    return math.ceil(math.log2((b-a)/e)) # use int() lost -1 iter, so I use math.ceil

epsilon = 1e-10
def bs(start, end, iter = 0):
    mid = (start + end) / 2

    if abs(f(mid)) < epsilon:
        return mid, iter

    if f(mid) * f(start) < 0 and f(mid) * f(end) < 0:
        print("Impossible case")
        return None, None

    if f(mid) * f(start) < 0:  # root is in left half
        return bs(start, mid, iter + 1)
    else:  # root is in right half
        return bs(mid, end, iter + 1)

START, END = 1, 4
root, number_of_iter = bs(START, END)
print("O(n):", check_complexity(START, END, epsilon))
print("root:", root)
print("number_of_iter:", number_of_iter)