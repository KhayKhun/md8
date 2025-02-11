import random

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

print(A)
print(known_sol)
print(rhs_vector)