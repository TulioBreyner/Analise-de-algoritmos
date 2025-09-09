import time
import numpy as np

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

def tempo_execucao(arr):
    inicio = time.time()
    
    merge_sort(arr.copy())

    fim = time.time()

    return fim - inicio

sizes = [ 10, 100, 1000, 5000, 10000, 50000, 100000]
for i in range(0, len(sizes)):
    array = np.random.randint(0, 10000, size=sizes[i])
    print(f"Tempo de execução para o array com {sizes[i]} posições: {tempo_execucao(array)}")