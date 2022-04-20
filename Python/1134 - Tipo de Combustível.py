al = gas = dis = 0
while True:
    cod = int(input())
    if cod == 4:
        break
    elif cod == 1:
        al += 1
    elif cod == 2:
        gas += 1
    elif cod == 3:
        dis += 1
print("MUITO OBRIGADO")
print(f"Alcool: {al}")
print(f"Gasolina: {gas}")
print(f"Diesel: {dis}")