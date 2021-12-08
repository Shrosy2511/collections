import random

def MenM(aantal):
    zak = []
    kleuren = ['groen', 'blauw', 'oranje', 'bruin']
    for i in range(aantal):
        zak.append(random.choice(kleuren))
    return zak

hoeveel = int(input('hoeveel m&ms wil je? '))

print(MenM(hoeveel))