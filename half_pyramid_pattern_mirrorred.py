# Half Pyramid Pattern Mirrored
n = 5
a = 2*n-2
for i in range(n):
    for j in range(a):
        print(" ", end="")
    a -= 2
    for j in range(i+1):
        print("*", end=" ")
    print()
