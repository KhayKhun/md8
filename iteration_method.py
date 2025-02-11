import random

def isDDM(A):
    N = len(A)
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += abs(A[i][j])
        row_sum -= abs(A[i][i])
        if abs(A[i][i]) < row_sum:
            return False
    return True

def generate_matrix(N):
    A = []
    for _ in range(N):
        row = [random.randint(1, 5) for _ in range(N)]
        A.append(row)
    return A

def generate_rhs(A, known_sol):
    N = len(A)
    b = []
    for i in range(N):
        total = 0.0
        for j in range(N):
            total += A[i][j] * known_sol[j]
        b.append(total)
    return b
    
def jacobi_iteration(A, b, initial_guess):
    N = len(A)
    current_guess = initial_guess[:]  # copy of previous X
    for iteration in range(10):
        new_x = [0] * N

        for i in range(N): # i for row
            # Compute the part of A[i][*] * current_guess excluding j = i (row index == col index)

            total = 0 # total except diagonal ones
            for j in range(N):
                if j != i:
                    total += A[i][j] * current_guess[j]
            new_x[i] = (b[i] - total) / A[i][i]

        diff = max(abs(new_x[i] - current_guess[i]) for i in range(N))
        print(f"Iteration {iteration}, current_guess = {new_x}, diff = {diff}")

        if diff < 1e-6: return new_x

        current_guess = new_x

    return current_guess

N = 3

A = []
while True:
    a = generate_matrix(N)
    if isDDM(a):
        A = a
        break

known_sol = [float(i + 1) for i in range(N)]
b = generate_rhs(A, known_sol)

print("A:", A)
print("RHS:", b)
print()

initial_guess = [ known_sol[i] + random.uniform(-0.5, 0.5) for i in range(N) ]

print("init guess:", initial_guess)
print()

res = jacobi_iteration(A, b, initial_guess)

print(res, known_sol)