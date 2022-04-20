hmif = input().split()
H_inicial = int(hmif[0])
H_final = int(hmif[1])

horas = H_final - H_inicial

if H_inicial + 1 == H_final:
    horas = 0
if horas < 0:
    horas  = 24 + horas

if H_inicial == H_final:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print(f"O JOGO DUROU {horas} HORA(S)")