while True:
    X = int(input())
    for c in range(1, X+1):
        if c == X:
            print(c)
        else:
            print(c, end=" ")
    if X == 0:
        break