# Full Pyramid Pattern
n = 5

a = n - 1
for i in range(n):
    for j in range(a):
        print(" ", end="")
    a -= 1
    for j in range(i+1):
        print("*", end=" ")
    print()
