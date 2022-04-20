n = input().split()
l = [int(n[0]), int(n[1])]
l.sort()
if l[1] % l[0] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")