# essa está errada, quando um ponto x é igual a 0 ele está no eixo Y e nao no eixo x
v = input().split()
x = float(v[0])
y = float(v[1])
if x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")