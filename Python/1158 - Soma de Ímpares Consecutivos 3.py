N = int(input())
for c in range(1, N+1):
    count = 0
    s = 0
    xy = input().split()
    X = int(xy[0])
    Y = int(xy[1])
    
    while count < Y:
        if X % 2 == 1:
            count +=1
            s += X
        X += 1
    print(s)