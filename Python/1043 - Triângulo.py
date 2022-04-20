v = input().split()
A = [float(v[0]), float(v[1]), float(v[2])]
B = [float(v[0]), float(v[1]), float(v[2])]
A.sort()
if A[2] < A[0] + A[1]:
    print(f"Perimetro = {(A[0] + A[1] + A[2]):.1f}")
else:
    print(f"Area = {(((B[0] + B[1]) *  B[2]) / 2):.1f}")