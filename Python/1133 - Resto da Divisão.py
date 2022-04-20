X = int(input())
Y = int(input())
v = [X, Y]
v.sort()
for c in range(v[0]+1, v[1]):
    if c % 5 == 2 or c % 5 == 3:
        print(c)