import time
import numpy as np

def selection_sort(v):
    n = len(v)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if v[j] < v[menor]:
                menor = j
        if i != menor:
            v[i], v[menor] = v[menor], v[i]  

def tempo_execucao(arr):
    inicio = time.time()
    selection_sort(arr.copy()) 
    fim = time.time()
    return fim - inicio

sizes = [ 10, 100, 1000, 5000, 10000, 50000, 100000]
for n in sizes:
    array = np.random.randint(0, 10000, size=n)
    tempo = tempo_execucao(array)
    print(f"Tempo de execução para o array com {n} posições: {tempo:.6f} segundos")
