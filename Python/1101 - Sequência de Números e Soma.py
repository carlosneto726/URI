x = 0
while True:
    MN = input().split()
    M = int(MN[0])
    N = int(MN[1])
    l = [M, N]
    l.sort()
    if M == 0 or N == 0 or M < 0 or N < 0:
        break
    for c in range(l[0], l[1] + 1):
        print(c, end=" ")
        x += c
    print(f"Sum={x}")
    x = 0