N = int(input())
for c in range(1, N+1):
    n = int(input())
    if n % 2 == 1 and n > 0:
        print("ODD POSITIVE")
    if n % 2 == 1 and n < 0:
        print("ODD NEGATIVE")
    if n % 2 == 0 and n > 0:
        print("EVEN POSITIVE")
    if n % 2 == 0 and n < 0:
        print("EVEN NEGATIVE")
    if n == 0:
        print("NULL")