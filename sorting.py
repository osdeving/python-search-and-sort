def selection_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            lista[j], lista[min_index] = lista[min_index], lista[j]

def bubble_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1):
            if(lista[i] > lista[i+1]):
                # swap previous with next element
                lista[i], lista[i+1] = lista[i+1], lista[i]


