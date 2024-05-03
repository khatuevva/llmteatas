from random import randint

def bubble_metod(array):
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

a = [randint(1, 99) for n in range(10)]
print(a)
bubble_metod(a)
print(a)