import random

liste = [random.randrange(1,101,1) for _ in range(random.randrange(5,31,1))]

print("entrée : ", liste)

def quicksorting(array):
    if (len(array) > 0):
        wall = 0
        pivot = len(array) - 1
        for i in range(len(array)):
            if array[i] < array[pivot]:
                array[i], array[wall] = array[wall], array[i]
                wall += 1
            elif i == pivot:
                array[wall], array[pivot] = array[pivot], array[wall]
                array[:wall] = quicksorting(array[:wall])
                array[wall+1:] = quicksorting(array[wall+1:])
    return array

print("sortie : ", quicksorting(liste))