# Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. 
# Calcule e imprima a média semestral. 
# O programa só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). 
# Cada nota deve ser validada separadamente.

# No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, 
# solicitando ao usuário que informe um código (1 ou 2) indicando se ele deseja ou não executar o algoritmo novamente, 
# (aceitar apenas os código 1 ou 2). 
# Se for informado o código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, 
# caso contrário o programa deve ser encerrado.

new = True
l = []
while True:
    #condição para caso tenha mais de 2 valores na lista "l".
    if len(l) < 2:
        n = float(input())
        #condição para, caso o valor seja válido, colocar valor, lido na linha de cima, na lista "l".
        if 0 <= n <= 10:
            l.append(n)
        #condição para caso o valor da variável lida "n" seja inválida.
        else:
            print("nota invalida")
    #condição para caso a quantidade de elementos da lista "l" igual á 2.
    elif len(l) == 2:
        print(f"media = {((l[0] + l[1]) / 2):.2f}")
        #laço de repetição para a condição de caso "novo calculo (1-sim 2-nao)" for diferente de 1 ou 2 repetir.
        while new:
            print("novo calculo (1-sim 2-nao)")
            X = int(input())
            if X == 1 or X == 2:
                new = False
        if X == 2:
            break
        elif X == 1:
            new = True
            l = []