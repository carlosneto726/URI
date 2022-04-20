salary = float(input())
if 0 < salary <= 400.00:
    percent = 15
elif 400.00 < salary <= 800.00:
    percent = 12
elif 800.00 < salary <= 1200.00:
    percent = 10
elif 1200.00 < salary <= 2000.00:
    percent = 7
elif salary > 2000.00:
    percent = 4
aumento = ((salary * percent) / 100) + salary
reajusto = aumento - salary
print(f"Novo salario: {aumento:.2f}")
print(f"Reajuste ganho: {reajusto:.2f}")
print(f"Em percentual: {percent} %")