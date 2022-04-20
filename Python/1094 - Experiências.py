R = S = C = 0
N = int(input())
for c in range(1, N+1):
    xp = input().split()
    if xp[1] == 'R':
        R += int(xp[0])
    if xp[1] == 'S':
        S += int(xp[0])
    if xp[1] == 'C':
        C += int(xp[0])
print(f"Total: {R+S+C} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {((C / (R+S+C)) * 100):.2f} %")
print(f"Percentual de ratos: {((R / (R+S+C)) * 100):.2f} %")
print(f"Percentual de sapos: {((S / (R+S+C)) * 100):.2f} %")