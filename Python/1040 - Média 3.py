notas = input().split()
N1 = float(notas[0])
N2 = float(notas[1])
N3 = float(notas[2])
N4 = float(notas[3])
M = ((2 * N1) + (3 * N2) + (4 * N3) + (1 * N4)) / 10
print(f"Media: {M:.1f}")
if M >= 7.0:
    print("Aluno aprovado.")
elif M < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    MF = (M + exame) / 2
    if MF >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {MF:.1f}")
