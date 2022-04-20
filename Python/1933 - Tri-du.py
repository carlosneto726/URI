c1c2 = input().split(" ")
c1 = int(c1c2[0])
c2 = int(c1c2[1])
c_aux = 0
if c1 == c2:
    print(c1)
elif c1 != c2:
    if c1 > c2:
        print(c1)
    else:
        print(c2)