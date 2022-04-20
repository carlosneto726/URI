T = int(input())
for c in range(0, T):
    pabg12 = input().split()
    pa = int(pabg12[0])
    pb = int(pabg12[1])
    g1 = float(pabg12[2])/100
    g2 = float(pabg12[3])/100
    anos = 0
    while pa <= pb:
        pa += int(pa * g1)
        pb += int(pb * g2)
        anos += 1
        if anos > 100:
            break
    if anos <= 100:
        print(anos, 'anos.')
    else:
        print("Mais de 1 seculo.")
        