bon = arq = mus = des = 0
testes = int(input())
for c in range(0, testes):
    e, g, h = input().split(" ")
    
    if g == "bonecos":
        bon += int(h)

    if g == "arquitetos":
        arq += int(h)

    if g == "musicos":
        mus += int(h)

    if g == "desenhistas":
        des += int(h)
    
brinquedos_por_dia = int(bon / 8) + int(arq / 4) + int(mus / 6) + int(des / 12)
print(brinquedos_por_dia)