impar = []
par = []
for c in range(0, 15):
    N = int(input())

    if N % 2 == 0:
        par.append(N)
    else:
        impar.append(N)
    
    if len(impar) >= 5:
        for im in range(0, 5):
            print(f"impar[{im}] = {impar[im]}")
        impar = []
    elif len(par) >= 5:
        for pa in range(0, 5):
            print(f"par[{pa}] = {par[pa]}")
        par = []

for im2 in range(0, len(impar)):
    print(f"impar[{im2}] = {impar[im2]}")

for pa2 in range(0, len(par)):
    print(f"par[{pa2}] = {par[pa2]}")
