dia1 = input().split()
tempo1 = input().split(" : ")

dia2 = input().split()
tempo2 = input().split(" : ")

d1 = int(dia1[1])
d2 = int(dia2[1])

h1 = int(tempo1[0])
m1 = int(tempo1[1])
s1 = int(tempo1[2])

h2 = int(tempo2[0])
m2 = int(tempo2[1])
s2 = int(tempo2[2])

dias = d2 - d1
horas = h2 - h1
minutos = m2 - m1
segundos = s2 - s1

if segundos < 0:
    segundos = 60 + segundos
    minutos = minutos - 1

if minutos < 0:
    minutos = 60 + minutos
    horas = horas - 1

if horas < 0:
    horas  = 24 + horas
    dias = dias - 1

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")