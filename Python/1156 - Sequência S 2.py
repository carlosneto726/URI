s = 0
numerador = 1
denominador = 1
while numerador <= 39:
    s += numerador / denominador
    numerador += 2
    denominador += denominador
print(f"{s:.2f}")