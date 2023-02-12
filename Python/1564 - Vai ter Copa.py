while True:
    try:
        numero = int(input())
        if numero < 1:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except EOFError:
        break