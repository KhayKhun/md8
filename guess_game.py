import random
N = 2

A = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randint(1,5))
    A.append(row)

seeds = [random.randint(1,5), random.randint(1,5)]
b = [
    A[0][0] * seeds[0] + A[0][1] * seeds[1],
    A[1][0] * seeds[0] + A[1][1] * seeds[1]
]

print(f"Metrix A:{A}\n Vector b:{b}")

solved = False
while not solved:
    x = []
    for i in range(N):
        x.append(int(input(f"Enter x:{i+1}: ")))
    print(f"Your solution: {x}")

    test1 = A[0][0] * x[0] + A[0][1] * x[1]
    test2 = A[1][0] * x[0] + A[1][1] * x[1]

    if test1 == b[0] and test2 == b[1]:
        print("Correct")
        solved = True