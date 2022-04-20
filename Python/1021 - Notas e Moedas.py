N = float(input())
cem = cinquenta = vinte = dez = cinco = dois = 0
um = cinquenta_cent = vinte_cent = dez_cent = cinco_cent = um_cent = 0
if N >= 100:
    cem = int(N / 100)
    N = N - (cem * 100)
if N >= 50:
    cinquenta = int(N / 50)
    N = N - (cinquenta * 50)
if N >= 20:
    vinte = int(N / 20)
    N = N - (vinte * 20)
if N >= 10:
    dez = int(N / 10)
    N = N - (dez * 10)
if N >= 5:
    cinco = int(N / 5)
    N = N - (cinco * 5)
if N >= 2:
    dois = int(N / 2)
    N = N - (dois * 2)
if N >= 1:
    um = int(N / 1)
    N = N - (um * 1)
if N >= 0.50:
    cinquenta_cent = int(N / 0.50)
    N = N - (cinquenta_cent * 0.50)
if N >= 0.25:
    vinte_cent = int(N / 0.25)
    N = N - (vinte_cent * 0.25)
if N >= 0.10:
    dez_cent = int(N / 0.10)
    N = N - (dez_cent * 0.10)
if N >= 0.05:
    cinco_cent = int(N / 0.05)
    N = N - (cinco_cent * 0.05)    
um_cent = int((N + 0.001) * 100)
print("NOTAS:")
print(f"{cem} nota(s) de R$ 100.00")
print(f"{cinquenta} nota(s) de R$ 50.00")
print(f"{vinte} nota(s) de R$ 20.00")
print(f"{dez} nota(s) de R$ 10.00")
print(f"{cinco} nota(s) de R$ 5.00")
print(f"{dois} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{um} moeda(s) de R$ 1.00")
print(f"{cinquenta_cent} moeda(s) de R$ 0.50")
print(f"{vinte_cent} moeda(s) de R$ 0.25")
print(f"{dez_cent} moeda(s) de R$ 0.10")
print(f"{cinco_cent} moeda(s) de R$ 0.05")
print(f"{um_cent} moeda(s) de R$ 0.01")