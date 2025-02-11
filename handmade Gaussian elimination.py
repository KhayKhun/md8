import random

# Step 0: Generate system
N = 5
A = []
for _ in range(N):
    row = [random.randint(1, 5) for _ in range(N)]
    A.append(row)

known_sol = [i + 1 for i in range(N)]

rhs_vector = []
for i in range(N):
    row_sum = 0
    for j in range(N):
        row_sum += A[i][j] * known_sol[j]
    rhs_vector.append(row_sum)

print("Initial matrix A:")
for row in A:
    print(row)
print("Initial RHS vector b:", rhs_vector)

# Step 1: elimination
for k in range(N):
    if A[k][k] == 0:
        for r in range(k + 1, N):
            if A[r][k] != 0:
                # swap entire rows in A
                A[k], A[r] = A[r], A[k]
                # swap corresponding entries in b
                rhs_vector[k], rhs_vector[r] = rhs_vector[r], rhs_vector[k]
                break
    
    pivot = A[k][k]
    if pivot == 0:
        continue
    
    for i in range(k+1, N):
        factor = A[i][k] / pivot
        for j in range(k, N):
            A[i][j] = A[i][j] - factor * A[k][j]
        rhs_vector[i] -= factor * rhs_vector[k]
    
    print(f"\nAfter eliminating column {k}:")
    for row in A:
        print([x for x in row])
    print("rhs:", [x for x in rhs_vector])

# Step 3: backward substitution
x_solution = [0 for _ in range(N)]
for row_index in reversed(range(N)):
    sum_ax = 0
    for col_index in range(row_index + 1, N):
        sum_ax += A[row_index][col_index] * x_solution[col_index]
    
    if A[row_index][row_index] == 0:
        print(f"A[{row_index}][{row_index}] is zero.")
        x_solution[row_index] = 0
    else:
        x_solution[row_index] = (rhs_vector[row_index] - sum_ax) / A[row_index][row_index]

print("backward substitution:", x_solution)

# Step 4: Testing
print("--- Testing ---")

diff = [abs(known_sol[idx] - x_solution[idx]) for idx in range(N)]
print("Computed solution:     ", x_solution)
print("Known solution:", known_sol)
print("Difference:  ", diff)

# compute residual r = A*x_solution - b
Ax = []
for i in range(N):
    row_val = 0
    for j in range(N):
        row_val += A[i][j] * x_solution[j]
    Ax.append(row_val)

r = [Ax[i] - rhs_vector[i] for i in range(N)]
print("residual:", r)