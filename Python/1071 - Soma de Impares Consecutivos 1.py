s = 0
X = int(input())
Y = int(input())
for c in range(Y+1, X):
    if c % 2 == 1:
        s = s + c
print(s)