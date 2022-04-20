p1 = input()
p2 = input()
p3 = input()
if p1 == "vertebrado":

    if p2 == "ave":

        if p3 == "carnivoro":
            animal = 'aguia'
        else:
            animal = 'pomba'

    else:

        if p3 == "onivoro":
            animal = "homem"
        else:
            animal = "vaca"

else:

    if p2 == "inseto":

        if p3 == "hematofago":
            animal = "pulga"
        else:
            animal = "lagarta"
    else:
        
        if p3 == "hematofago":
            animal = "sanguessuga"
        else:
            animal = "minhoca"

print(animal)