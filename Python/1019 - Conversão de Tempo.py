N = int(input())
h = ((N / 60) / 60)
horas = int(h)
m = (h - horas) * 60
minutos = int(m)
s = (m - minutos) * 60
print(f"{horas}:{minutos}:{s:.0f}")