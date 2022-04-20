n = int(input())
for c in range(0, n):
    soma = input().split("+")
    if soma[0] == "P=NP":
        print("skipped")
    else:
        print(int(soma[0]) + int(soma[1]))