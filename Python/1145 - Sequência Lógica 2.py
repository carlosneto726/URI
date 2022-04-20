XY = input().split()
X = int(XY[0])
Y = int(XY[1])
i = 0
while True:
    for c in range(1, X + 1):
        i += 1
        if c == X:
            print(i)
        else:
            print(i, end=" ")
    if i >= Y:
        break
    