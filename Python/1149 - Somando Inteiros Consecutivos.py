l = []
N = input().split()
for c in range(0, len(N)):
    if int(N[c]) > 0:
        l.append(N[c])
res = int(N[0])
x = 0
for i in range(0, int(l[1])):
    x = x + i + res
print(x)
