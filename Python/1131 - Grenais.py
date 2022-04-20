grenais = inter = gremio = empates = 0
while True:
    gols = input().split()
    print("Novo grenal (1-sim 2-nao)")
    sino = int(input())
    grenais += 1
    if int(gols[0]) > int(gols[1]):
        inter += 1
    elif int(gols[1]) > int(gols[0]):
        gremio += 1
    elif int(gols[0]) == int(gols[1]):
        empates += 1
    if sino == 2:
        break
print(f"{grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empates}")
if inter > gremio:
    print(f"Inter venceu mais")
elif gremio > inter:
    print(f"Gremio venceu mais")
else:
    print(f"Nao houve vencedor") 