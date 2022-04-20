p = i = pos = neg = 0
for c in range(0, 5):
    n = int(input())
    if n % 2 == 0:
        p += 1
    if n % 2 == 1:
        i += 1
    if n > 0:
        pos += 1
    if n < 0:
        neg += 1
print(f"{p} valor(es) par(es)") 
print(f"{i} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)") 
print(f"{neg} valor(es) negativo(s)")
