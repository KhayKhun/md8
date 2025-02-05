# when the function converges, the output of  g(x)  does not change anymore.
import math

eps = 1e-3

def fixed_point_iteration(g):
    xk = -0.4 # initial x0 

    for k in range(100):
        x_next = g(xk)
        difference = abs(x_next - xk)

        if difference <= eps:
            print(f"itera {k}: Xk = {xk}, Xk+1 = {x_next}, difference = {difference}")
            break

        xk = x_next

fixed_point_iteration(lambda x: (-1 * (x**2 - x - 2) / 6) + x)
fixed_point_iteration(lambda x: (x + 2) / 2)
fixed_point_iteration(lambda x: math.sqrt(x + 2)) # x^2 - x - 2 = (x-2)(x+1) -> root is 2 or -1
# fixed_point_iteration(lambda x: x**2 - 2)