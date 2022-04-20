while True:
    try:
        num = int(input())
        res = num - 1
        print(res)
    except EOFError:
        break
