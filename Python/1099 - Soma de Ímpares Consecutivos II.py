count = 0
N = int(input())
for c in range(1, N + 1):
    XY = input().split()
    X = int(XY[0])
    Y = int(XY[1])
    l = [X, Y]
    l.sort()
    for i in range(l[0]+1, l[1]):
        if i % 2 == 1:
            count += i
    print(count)
    count = 0