liste = [5,8,7,3,2,4,6,1]

for i in range(len(liste)):
    val = liste[i]
    j = i
    while j > 0 and liste[j - 1] > val:
        liste[j] = liste[j-1]
        j -= 1
    liste[j] = val
print(liste)