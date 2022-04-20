N = int(input())
for c in range(1, N + 1):
    notas = input().split()
    l = [float(notas[0]), float(notas[1]), float(notas[2])]
    print(f"{(((l[0] * 2) + (l[1] * 3) + (l[2] * 5)) / 10):.1f}" )
