import time
import numpy as np

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


def tempo_execucao(arr):
    inicio_tempo = time.time()
    
    quick_sort(arr, 0, len(arr) - 1)

    fim_tempo = time.time()
    return fim_tempo - inicio_tempo


sizes = [ 10, 100, 1000, 5000, 10000, 50000, 100000]
for n in sizes:
    array = np.random.randint(0, 10000, size=n)
    tempo = tempo_execucao(array.copy())
    print(f"Tempo de execução para o array com {n} posições: {tempo:.6f} segundos")
