a = input().split()
H = int(a[0])
Z = int(a[1])
L = int(a[2])

if H < Z < L or L < Z < H:
    print("zezinho")
elif Z < H < L or L < H < Z:
    print("huguinho")
elif H < L < Z or Z < L < H:
    print("luisinho")
