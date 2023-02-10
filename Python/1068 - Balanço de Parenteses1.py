# correct: a+(b*c)-2-a
# correct: (a+b*(2-c)-2+a)*2 
# incorrect: (a*b-(2+c) 
# incorrect: 2*(3-a))  
# incorrect: )3+b*(2-c)( 

while True:

    inp = input()
    exp = ''
    for char in inp:
        if char == '(' or char == ')':
            exp += char

    flag = True
    count = 0

    for i in range(len(exp)):
        if (exp[i] == '('):
            count += 1
        else:
            count -= 1

        if (count < 0):
            flag = False
            break

    if (count != 0):
        flag = False


    if flag:
        print('correct')
    else:
        print('incorrect')


