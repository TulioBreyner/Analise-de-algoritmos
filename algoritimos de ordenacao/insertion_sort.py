import time
import numpy as np

def insertion_sort(v):
    n = len(v)
    for i in range(1, n):
        aux = v[i]
        j = i
        while j > 0 and aux < v[j - 1]:
            v[j] = v[j - 1]
            j -= 1
        v[j] = aux

def tempo_execucao(arr):
    inicio = time.time()
    insertion_sort(arr.copy()) 
    fim = time.time()
    return fim - inicio

sizes = [ 10, 100, 1000, 5000, 10000, 50000, 100000]
for n in sizes:
    array = np.random.randint(0, 10000, size=n)
    tempo = tempo_execucao(array)
    print(f"Tempo de execução para o array com {n} posições: {tempo:.6f} segundos")
