while True:
    s = 0
    c = 0
    X = int(input())
    if X == 0:
        break
    while c < 5:
        if X % 2 == 0:
            s += X   
            c += 1
        X += 1
    print(s)