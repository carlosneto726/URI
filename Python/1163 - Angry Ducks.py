from math import sin, cos, sqrt

pi = 3.14159
g = 9.80665

while True:
    try:
        altura = float(input())
        nlogonia = input().split()
        p1 = int(nlogonia[0])
        p2 = int(nlogonia[1])

        tentativas = int(input())
        for i in range(0, tentativas):
            angulo_velocidade = input().split()
            angulo = float(angulo_velocidade[0])
            velocidade = float(angulo_velocidade[1])

            vx = cos((angulo * pi / 180 )) * velocidade
            vy = sin((angulo * pi / 180)) * velocidade

            a = (g / 2) * -1
            b = vy
            c = altura
            delta = (b**2) - (4 * a * c)
            
            tempo1 = ((-1 * b) + sqrt(delta)) / (2 * a)
            tempo2 = ((-1 * b) - sqrt(delta)) / (2 * a)
            tempo = 0
            
            if tempo1 > tempo2:
                tempo = tempo1
            else:
                tempo = tempo2
            
            alcance = vx * tempo

            if alcance >= p1 and alcance <= p2:
                res = "DUCK"
            else:
                res = "NUCK"

            print(f"{alcance:.5f} -> {res}")

    except (EOFError):
        break
