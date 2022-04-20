time = int(input())
for times in range(0, time):
    N = int(input())
    if N == 0:
        print("Fib(0) = 0")
    else:
        l = []
        x = 0
        y = 1
        z = 0
        for c in range(0, N):
            x = y
            y = z
            z = x + y
            l.append(z)
        print(f"Fib({N}) = {l[N - 1]}")

