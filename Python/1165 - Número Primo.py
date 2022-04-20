times = int(input())
for time in range(0, times):
    c = 1
    N = int(input())
    if N == 2:
        print(f"2 eh primo")
    else:
        while True:
            c += 1
            if N % c == 0:
                res = "nao eh primo"
                break
            else:
                res = "eh primo"
            if c ==  N - 1:
                break
        print(f"{N} {res}")