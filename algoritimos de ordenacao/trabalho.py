import time
import numpy as np

###########################
# BUBBLE SORT
###########################
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


###########################
# SELECTION SORT
###########################
def selection_sort(v):
    n = len(v)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if v[j] < v[menor]:
                menor = j
        if i != menor:
            v[i], v[menor] = v[menor], v[i]  


###########################
# INSERTION SORT
###########################
def insertion_sort(v):
    n = len(v)
    for i in range(1, n):
        aux = v[i]
        j = i
        while j > 0 and aux < v[j - 1]:
            v[j] = v[j - 1]
            j -= 1
        v[j] = aux


###########################
# MERGE SORT
###########################
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


###########################
# QUICK SORT
###########################
def particiona(v, inicio, fim):
    esq = inicio
    dir = fim
    pivo = v[inicio]

    while esq < dir:
        while esq <= fim and v[esq] <= pivo:
            esq += 1
        while dir >= 0 and v[dir] > pivo:
            dir -= 1
        if esq < dir:
            v[esq], v[dir] = v[dir], v[esq]

    v[inicio], v[dir] = v[dir], pivo
    return dir

def quick_sort(v, inicio, fim):
    if fim > inicio:
        pivo = particiona(v, inicio, fim)
        quick_sort(v, inicio, pivo - 1)
        quick_sort(v, pivo + 1, fim)


###########################
# TESTES
###########################
def tempo_execucao(arr, alg):
    match (alg):
        case "bubble":
            inicio = time.time()
            bubble_sort(arr)
            fim = time.time()
            return fim - inicio
        case "selection":
            inicio = time.time()
            selection_sort(arr) 
            fim = time.time()
            return fim - inicio
        case "insertion":
            inicio = time.time()
            insertion_sort(arr) 
            fim = time.time()
            return fim - inicio
        case "merge":
            inicio = time.time()
            merge_sort(arr)
            fim = time.time()
            return fim - inicio
        case "quick":
            inicio_tempo = time.time()        
            quick_sort(arr, 0, len(arr) - 1)
            fim_tempo = time.time()
            return fim_tempo - inicio_tempo
        case _:
            return "algoritimo de ordenação não encontrado"

sizes = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
algoritimos = ["bubble", "selection", "insertion", "merge", "quick"]
for n in sizes:
    print("-"*50)
    array = np.random.randint(0, 10000, size=n)
    for alg in algoritimos:
        tempo = tempo_execucao(array.copy(), alg)
        print(f"Array com {n} posições: {tempo:.6f} segundos | {alg}")
