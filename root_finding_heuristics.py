def f(x):
    return x**4 + 3*x**3 + x**2 - 2*x - 0.5

def bisection(f, left, right, epsilon=1e-10):
    mid = (left + right) / 2

    if abs(f(mid)) < epsilon:
        return mid

    if f(left) * f(mid) < 0: # root is in left
        return bisection(f, left, mid, epsilon)
    else: # root is in right
        return bisection(f, mid, right, epsilon)
# in each subintervel, find the root and sign change. If sign changed, dive search root using binary search
def find_all_roots(f, start, end, num_subintervals=100, epsilon=1e-10):
    
    interval_length = (end - start) / num_subintervals # (5 - (-5))/200 -> 0.05
    roots = []

    for i in range(num_subintervals):
        a = start + i * interval_length # 0.25, 0.3, 0.35, ... -> + 0.05
        b = a + interval_length # 0.3, 0.35, ... -> a + 0.05

        fa = f(a)
        fb = f(b)

        if abs(fa) < epsilon:
            roots.append(a)
        elif abs(fb) < epsilon:
            roots.append(b)
        # If there's a sign change, run bisection
        if fa * fb < 0:
            root = bisection(f, a, b, epsilon)
            roots.append(root)

    return roots

START, END = -5, 5
EPSILON = 1e-10
N = 200

all_roots = find_all_roots(f, START, END, num_subintervals=N, epsilon=EPSILON)

print("found roots:")
for r in all_roots:
    print(f"x ≈ {r}")