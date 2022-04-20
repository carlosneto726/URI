T = int(input())
winner = ""
for caso in range(0, T):
    sr = input().split()
    if sr[0] == sr[1]:
        winner = "De novo!"
    elif sr[0] == "tesoura" and sr[1] == "papel":
        winner = "Bazinga!"
    elif sr[0] == "papel" and sr[1] == "pedra":
        winner = "Bazinga!"
    elif sr[0] == "pedra" and sr[1] == "lagarto":
        winner = "Bazinga!"
    elif sr[0] == "lagarto" and sr[1] == "Spock":
        winner = "Bazinga!"
    elif sr[0] == "Spock" and sr[1] == "tesoura":
        winner = "Bazinga!"
    elif sr[0] == "tesoura" and sr[1] == "lagarto":
        winner = "Bazinga!"
    elif sr[0] == "lagarto" and sr[1] == "papel":
        winner = "Bazinga!"
    elif sr[0] == "papel" and sr[1] == "Spock":
        winner = "Bazinga!"
    elif sr[0] == "Spock" and sr[1] == "pedra":
        winner = "Bazinga!"
    elif sr[0] == "pedra" and sr[1] == "tesoura":
        winner = "Bazinga!"
    else:
        winner = "Raj trapaceou!"
    print(f"Caso #{caso+1}: {winner}")
