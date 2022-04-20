i = 1
j = 7
while True:
    print(f"I={i} J={j}")
    print(f"I={i} J={j-1}")
    print(f"I={i} J={j-2}")
    j += 2
    i += 2
    if i > 9:
        break