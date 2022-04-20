jogadas = int(input())
for jogada in range(0, jogadas):
    
    jogador1 = input()
    jogador2 = input()

    if jogador1 == "pedra" and jogador2 == "pedra":
        print("Sem ganhador")

    elif jogador1 == "ataque" and jogador2 == "ataque":
        print("Aniquilacao mutua")

    elif jogador1 == "papel" and jogador2 == "papel":
        print("Ambos venceram")

    elif jogador1 == "ataque" and jogador2 == "papel" or jogador2 == "pedra":
        print("Jogador 1 venceu")

    elif jogador2 == "ataque" and jogador1 == "pepel" or jogador1 == "pedra":
        print("Jogador 2 venceu")

    elif jogador1 == "pedra" and jogador2 == "papel":
        print("Jogador 1 venceu")

    elif jogador2 == "pedra" and jogador1 == "papel":
        print("Jogador 2 venceu")
