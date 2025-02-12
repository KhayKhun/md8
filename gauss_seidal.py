import random

def isSDDM(A):
    N = len(A)
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += abs(A[i][j])
        row_sum -= abs(A[i][i])
        if abs(A[i][i]) <= row_sum:
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

N = 3

def gauss_seidel(A, b, initial_guess):

    current_guess = initial_guess[:]  # Make a copy so we don't modify the original guess
    N = len(A)

    for k in range(10):
        for i in range(N):
            # sum up A[i][j]*current_guess[j] for j != i,
            # but note that some current_guess[j] may already be updated in this iteration!
            total = 0
            for j in range(N):
                if j != i:
                    total += A[i][j] * current_guess[j]
            
            # Update current_guess[i] using the newly updated values for j < i
            current_guess[i] = (b[i] - total) / A[i][i]

        # (Optional) print or store the intermediate result
        print(f"Iteration {k+1}: {current_guess}")

    return current_guess

A = []
while True:
    a = generate_matrix(N)
    if isSDDM(a):
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

res = gauss_seidel(A, b, initial_guess)

print(res, known_sol)