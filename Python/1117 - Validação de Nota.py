l = []
while True:
    n = float(input())
    if 0 <= n <= 10:
        l.append(n)
    else:
        print("nota invalida")
    if len(l) >= 2:
        break
print(f"media = {((l[0] + l[1]) / 2):.2f}")