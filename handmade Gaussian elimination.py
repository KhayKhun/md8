import random
import copy

# Generators
def generate_random_matrix(N):
    A = []
    for _ in range(N):
        row = [random.randint(1, 5) for _ in range(N)]
        A.append(row)
    return A

def generate_hilbert_matrix(N):
    H = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(1.0 / (i + j + 1))
        H.append(row)
    return H

def generate_rhs(A, known_sol):
    N = len(A)
    b = []
    for i in range(N):
        total = 0.0
        for j in range(N):
            total += A[i][j] * known_sol[j]
        b.append(total)
    return b

def forward_elimination(A, b):
    N = len(A)
    for pivot_idx in range(N):
        if A[pivot_idx][pivot_idx] == 0:
            for swap_idx in range(pivot_idx+1, N):
                if A[swap_idx][pivot_idx] != 0:
                    A[pivot_idx], A[swap_idx] = A[swap_idx], A[pivot_idx]
                    b[pivot_idx], b[swap_idx] = b[swap_idx], b[pivot_idx]
                    break
        
        pivot = A[pivot_idx][pivot_idx]
        if pivot == 0:
            continue
        
        # eliminate below pivot
        for row_below in range(pivot_idx+1, N):
            factor = A[row_below][pivot_idx] / pivot
            for col_below in range(pivot_idx, N):
                A[row_below][col_below] -= factor * A[pivot_idx][col_below]
            b[row_below] -= factor * b[pivot_idx]

def backward_substitution(A, b):
    N = len(A)
    x = [0] * N
    for row_idx in reversed(range(N)):
        sum_ax = 0.0
        for col_idx in range(row_idx+1, N):
            sum_ax += A[row_idx][col_idx] * x[col_idx]
        
        if A[row_idx][row_idx] == 0:
            x[row_idx] = 0.0
        else:
            x[row_idx] = (b[row_idx] - sum_ax) / A[row_idx][row_idx]
    return x

def test_solution(A_original, x_solution, b_original, known_solution):
    N = len(A_original)
    diffs = [abs(x_solution[i] - known_solution[i]) for i in range(N)]
    Ax = []
    for i in range(N):
        row_val = 0.0
        for j in range(N):
            row_val += A_original[i][j] * x_solution[j]
        Ax.append(row_val)
    residual = [Ax[i] - b_original[i] for i in range(N)]
    
    print("Computed solution:", x_solution)
    print("Known solution:   ", known_solution)
    print("Difference:       ", diffs)
    print("Residual:         ", residual)

def main(N):
    known_sol = [float(i+1) for i in range(N)]
    
    print(f"\nN = {N}\n")

    # random matrix
    A_rand = generate_random_matrix(N)
    rhs_rand = generate_rhs(A_rand, known_sol)
    
    # copy of originals for later usage
    A_rand_copy = copy.deepcopy(A_rand)
    b_rand_copy = copy.deepcopy(rhs_rand)
    
    forward_elimination(A_rand_copy, b_rand_copy)
    sol_rand = backward_substitution(A_rand_copy, b_rand_copy)
    
    print("Random Matrix---")
    test_solution(A_rand, sol_rand, rhs_rand, known_sol)
    
    # 2) Hilbert matrix
    A_hilbert = generate_hilbert_matrix(N)
    b_hilbert = generate_rhs(A_hilbert, known_sol)
    
    A_hilbert_copy = copy.deepcopy(A_hilbert)
    b_hilbert_copy = copy.deepcopy(b_hilbert)
    
    forward_elimination(A_hilbert_copy, b_hilbert_copy)
    sol_hilbert = backward_substitution(A_hilbert_copy, b_hilbert_copy)
    
    print("Hilbert Matrix---")
    test_solution(A_hilbert, sol_hilbert, b_hilbert, known_sol)

# Step 5: test diff N
for size in [3,5]:
    main(size)