n = input().split()
A = int(n[0])
B = int(n[1])
C = int(n[2])
D = int(n[3])
if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")