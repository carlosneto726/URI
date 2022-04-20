# os dois funcionam, mas o uri por algum motivo só aceitou o de baixo.

#feito por @Sailoggo
X = int(input())
Z = int(input())
while X > Z:
    Z = int(input())
c = 0
y = 0
while True:
    c = c + X
    X = X + 1
    y = y + 1
    if c > Z:
        break    
print(y)

# pego do Github https://github.com/NadiaaOliverr/Uri-Problem-Solutions/blob/master/Python/1150%20-%20Ultrapassando%20Z.py
X = int(input())
Z = int(input())
count = 0
j = 1
while Z <= X:
    Z = int(input())

count =  X
j = 1
aux = count
times = 0
while aux < Z:
    count = count + j
    #print('count: ' + str(count))
    aux = count + aux
    #print(aux)
    times +=1

print(times+1)

