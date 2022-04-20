N = int(input())
x = 0
y = 1
z = 0
for c in range(0, N):
    if c == N - 1:
        print(z)
    else:
        print(z, end=" ")
    x = y
    y = z
    z = x + y