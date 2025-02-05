import math

def f(x):
    return math.sqrt(x)

tolerance = 1e-6 

xk = 2  # initial x0 -> 2

for k in range(100):
    x_next = f(xk)  # Compute next value
    difference = abs(x_next - xk)  # Check how much x is changing

    print(f"Iteration {k}: Xk = {xk}, Xk+1 = {x_next}, Difference = {difference}")

    # if difference < tolerance:
    #     break
    if difference == 0:
        break

    xk = x_next