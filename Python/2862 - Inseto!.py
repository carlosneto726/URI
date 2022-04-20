testes = int(input())
for c in range(0, testes):
    energia = int(input())
    if energia > 8000:
        print("Mais de 8000!")
    elif energia <= 8000:
        print("Inseto!")