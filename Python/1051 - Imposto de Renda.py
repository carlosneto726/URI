tax1 = tax2 = tax3 = 0
sal1 = sal2 = sal3 = 0

sal = float(input())

if sal > 4500.00:
    sal1 = sal - 4500.00
    tax1 = (sal1 * 28) / 100

if sal > 3000.00:
    sal2 = (sal - 3000.00) - sal1
    tax2 = (sal2 * 18) / 100

if sal > 2000.00:
    sal3 = ((sal - 2000.00) - sal2) - sal1
    tax3 = (sal3 * 8) / 100

tax = tax1 + tax2 + tax3

if sal <= 2000.00:
    print("Isento")
else:
    print(f"R$ {tax:.2f}")