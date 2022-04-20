v = input().split()
n = [float(v[0]), float(v[1]), float(v[2])]
n.sort(reverse=True)
A = n[0]
B = n[1]
C = n[2]

if A >= B + C:
    print("NAO FORMA TRIANGULO")

elif A ** 2 > B ** 2 + C ** 2:
    print("TRIANGULO OBTUSANGULO")

if (A**2) == (B**2) + (C**2):
    print("TRIANGULO RETANGULO")

if (A**2) < (B**2) + (C**2):
    print("TRIANGULO ACUTANGULO")

if A == B == C:
    print("TRIANGULO EQUILATERO")

if A == B and C != A or A == C and B != A or B == C and A != B:
    print("TRIANGULO ISOSCELES")