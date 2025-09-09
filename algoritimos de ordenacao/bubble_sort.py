import time
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def tempo_execucao(arr):
    inicio = time.time()
    
    bubble_sort(arr.copy())

    fim = time.time()

    return fim - inicio

sizes = [ 10, 100, 1000, 5000, 10000, 50000, 100000]
for i in range(0, len(sizes)):
    array = np.random.randint(0, 10000, size=sizes[i])
    print(f"Tempo de execução para o array com {sizes[i]} posições: {tempo_execucao(array)}")