# Full Pyramid Pattern Mirrorred
n = 4
a = 2*n - 2

for i in range(n, -1, -1):
    for j in range(a, 0, -1):
        print(" ", end="")
    a += 1
    for j in range(i+1):
        print("*", end=" ")
    print()
