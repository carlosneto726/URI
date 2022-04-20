n = input().split()
code = int(n[0])
qtd = int(n[1])
prices = [4.00, 4.50, 5.00, 2.00, 1.50]
print(f"Total: R$ {((prices[code - 1]) * qtd):.2f}")
