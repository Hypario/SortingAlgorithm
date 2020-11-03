maliste = [5,3,2,1,4,5,8,7,9,3,65,21,33,456,231,15,452,23,231,325]

def selectionsort(liste):
    for i in range(len(liste)):
        minimum = i
        for j in range(i, len(liste)):
            if liste[minimum] > liste[j]:
                minimum = j
        liste[minimum], liste[i] = liste[i], liste[minimum]
    return liste

print("non-sorted :", maliste)
print("sorted :", selectionsort(maliste))