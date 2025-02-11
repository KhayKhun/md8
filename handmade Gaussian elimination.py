import random

# Step 0: Generate system
N = 3
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

# Step: 1
for k in range(N): # K for col
    if A[k][k] == 0:
        for r in range(k+1, N):
            if A[r][k] != 0:
                A[k], A[r] = A[r], A[k]  # Swap entire rows in A
                rhs_vector[k], rhs_vector[r] = rhs_vector[r], rhs_vector[k]  # Swap corresponding entries in rhs_vector
                break
    
    pivot = A[k][k]
    # If pivot is still zero (e.g., all below were zero), we won't proceed further in that column
    if pivot == 0:
        continue
    
    for i in range(k+1, N): # i for row
        factor = A[i][k] / pivot
        for j in range(k, N): # j for col
            A[i][j] = A[i][j] - factor * A[k][j]
        rhs_vector[i] = rhs_vector[i] - factor * rhs_vector[k]
    
    print(f"\nAfter eliminating column {k}:")
    for row in A:
        print([x for x in row])
    print("b:", [x for x in rhs_vector])