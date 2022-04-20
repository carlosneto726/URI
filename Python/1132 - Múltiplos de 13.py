m = 0
X = int(input())
Y = int(input())
XY = [X, Y]
XY.sort()
for c in range(XY[0], XY[1] + 1):
    if c % 13 != 0:
        m += c
print(m)