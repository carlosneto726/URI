c = i = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    c += idade
    i += 1
print(f"{(c / i):.2f}")
