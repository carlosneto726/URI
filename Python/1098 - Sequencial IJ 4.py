# pqp python desgraaaaaçaaaaaaa
sino = int(input("Qual método deseja?: Complexo e certo[1]. Simples e errado[2]."))
if sino == 1:
    i = 0
    while True:
        if i > 0.4 and i < 0.8 or i > 1.4 and i < 1.8:
            print(f"I={i:.1f} J={1+i:.1f}")
            print(f"I={i:.1f} J={2+i:.1f}")
            print(f"I={i:.1f} J={3+i:.1f}")
        elif i > 1.8 or i > 0.8 and i < 1.2:
            print(f"I={i:.0f} J={int(1+i)}")
            print(f"I={i:.0f} J={int(2+i)}")
            print(f"I={i:.0f} J={int(3+i)}")
        else:
            print(f"I={i} J={1+i}")
            print(f"I={i} J={2+i}")
            print(f"I={i} J={3+i}")
        i += 0.2
        if i > 2:
            break
elif sino == 2:
    i = 0
    while True:
        print(f"I={i} J={1+i}")
        print(f"I={i} J={2+i}")
        print(f"I={i} J={3+i}")
        i = i + 0.2
        if i > 2:
            break
else:
    print("Resposta Inválida.")