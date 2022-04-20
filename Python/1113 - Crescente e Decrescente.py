c = 0
while True:
    XY = input().split()
    X = int(XY[0])
    Y = int(XY[1])
    if X > Y:
        print("Decrescente")
    elif X < Y:
        print("Crescente")
    else:
        break