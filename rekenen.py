def rekenen():
    listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listTwo = [2, 4 , 6, 8, 10, 12, 14, 16, 18, 20]
    listThree = []

    for i in range(0, len(listOne)):
        print('---------------')
        print(listOne[i], '+',listTwo[i], '=', listOne[i]+listTwo[i])
    for i in range(0, len(listOne)):
        print('---------------')
        print(listOne[i], '-',listTwo[i], '=', listOne[i]-listTwo[i])
    for i in range(0, len(listOne)):
        print('---------------')
        print(listOne[i], 'x',listTwo[i], '=', listOne[i]*listTwo[i])
    for i in range(0, len(listOne)):
        print('---------------')
        print(listOne[i], '/',listTwo[i], '=', listOne[i]/listTwo[i])

rekenen()