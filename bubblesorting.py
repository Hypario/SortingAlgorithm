def bubblesorting(maliste):
    for i in range(len(maliste) - 1):
        for j in range(len(maliste) - 1 - i):
            if maliste[j] > maliste[j+1]:
                maliste[j], maliste[j+1] = maliste[j+1], maliste[j]
    return maliste

maliste = ['a', 'd', 'c', 'b']
print("non-sorted :", maliste)
print("sorted :", bubblesorting(maliste))