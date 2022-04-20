hmif = input().split()
H_inicial = int(hmif[0])
M_inicial = int(hmif[1])
H_final = int(hmif[2])
M_final = int(hmif[3])

horas = H_final - H_inicial
minutos = M_final - M_inicial

if minutos < 0:
    minutos = 60 + minutos
    horas = horas - 1
if H_inicial + 1 == H_final:
    horas = 0
if horas < 0:
    horas  = 24 + horas

if H_inicial == H_final == M_inicial == M_final:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")