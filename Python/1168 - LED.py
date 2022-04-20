for c in range(0, int(input())):
    leds = 0
    num = list(input())
    for i in num:
        if i == "0":
            leds += 6
        if i == "1":
            leds += 2
        if i == "2":
            leds += 5
        if i == "3":
            leds += 5
        if i == "4":
            leds += 4
        if i == "5":
            leds += 5
        if i == "6":
            leds += 6
        if i == "7":
            leds += 3
        if i == "8":
            leds += 7
        if i == "9":
            leds += 6

    print(f"{leds} leds")