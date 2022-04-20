l = []
x = z = 0
y = 1
times = int(input())
for time in range(0, times):
    n = int(input())
    if n == 0:
        print("Fib(0) = 0")
    else:
        while len(l) < n:
            x = y
            y = z
            z = x + y
            l.append(z)
        print(l)
        print(f"Fib({n}) = {l[n - 1]}")