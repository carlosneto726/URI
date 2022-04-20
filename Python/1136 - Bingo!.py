def rep(lista):
    lis = []
    for h in lista:
        if h not in lis:
            lis.append(h)
    lis.sort()
    return lis

while True:
    l = [0]
    nb = input().split(" ")
    n = int(nb[0])
    b = int(nb[1])

    if n == 0 and b == 0:
        break
    else:
        bng = input().split(" ")
        for c in range(0, b):
            for i in range(0, b):
                if i != c:
                    num = int(bng[c]) - int(bng[i])
                    if num > 0:
                        l.append(num)
        l.sort()
        newlist = rep(l)        
        for j in range(0, n+1):
            try:
                if newlist[j] != j:
                    print("N")
                    break
            except IndexError:
                print("N")
                break
        else:
            print("Y")
