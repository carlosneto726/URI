n = input().split(".")
formated = n[1] + "." + n[0]
if formated[0] == "0":
    formated.replace("0", "")
print(formated)