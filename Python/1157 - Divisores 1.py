N = int(input())
c = 0
while c != N:
    c = c + 1
    if N % c == 0:
        print(c)