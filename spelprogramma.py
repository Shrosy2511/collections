import random


def spelProgramma(spelList, minimaal, maximaal):
    spellen = []
    nummer = random.randint(minimaal,maximaal)
    for i in range(nummer):
        spellen.append(random.choice(spelList))
    return spellen
    
spellist = ['monopoly', 'yahtzee', 'bridge', 'poker', 'pesten', 'mens erger je niet', 'cluedo']

lijst = spelProgramma(spellist, 3, 10)
print(lijst)