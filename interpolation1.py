import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return math.sin(x) + 0.5 * math.cos(2*x)
interval = [1, 4]
m = 5

# Step 1
size = abs(interval[1]-interval[0])/m

# Step 2
x_vals = [interval[0] + size * i for i in range(1, m+1)]
y_vals = []

for x in x_vals:
    y_vals.append(f(x))


# Step 3
metrix_X = []

for i in range(m): # i for x_i
    row = []
    for j in range(m): # j for power of 0 to m-1 times
        row.append(x_vals[i]**j)
    metrix_X.append(row)

print("xs:", x_vals)
print("ys:", y_vals)
for r in metrix_X:
    temp = [round(val,2) for val in r]
    print(temp)

X_matrix = np.array(metrix_X)
Y_vector = np.array(y_vals)
A_coeffs = np.linalg.solve(X_matrix, Y_vector)

print("coefficients:", A_coeffs)

# Step 4
def interpolating_polynomial(x):
    return sum(A_coeffs[j] * x**j for j in range(m))

x_fine = np.linspace(interval[0], interval[1], 100)
y_fine = [f(x) for x in x_fine]
y_interpolated = [interpolating_polynomial(x) for x in x_fine]

plt.plot(x_fine, y_fine, label="Original Function f(x)")
plt.plot(x_fine, y_interpolated, label="Interpolation Polynomial")
# plt.scatter(x_vals, y_vals, color='red', label="Interpolation Points")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function Approximation using Polynomial Interpolation")
plt.grid()
plt.show()