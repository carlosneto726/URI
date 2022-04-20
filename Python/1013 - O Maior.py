print("Qual metodo deseja usar? Simples e compacto[1]. Complexo e Extensivo[2].")
N = int(input())
if N == 1:
    ABC = input().split()
    maior = [int(ABC[0]), int(ABC[1]), int(ABC[2])]
    maior.sort(reverse=True)
    print(f"{maior[0]} eh o maior")
elif N == 2:
    ABC = input().split()
    a = int(ABC[0])
    b = int(ABC[1])
    c = int(ABC[2])
    modulo_de_ab = a - b
    if modulo_de_ab < 0:
        modulo_de_ab = modulo_de_ab * -1
    maior_ab = ((a + b) + modulo_de_ab) / 2
    modulo_de_abc = maior_ab - c
    if modulo_de_abc < 0:
        modulo_de_abc = modulo_de_abc * -1
    maior_abc = ((maior_ab + c) + modulo_de_abc) / 2
    print(f"{maior_abc:.0f} eh o maior")
else:
    print("Resposta Inválida.")