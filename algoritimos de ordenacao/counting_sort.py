import time
import numpy as np

def counting_sort(v, k=10000):
    # Cria os baldes (inicialmente zerados)
    baldes = [0] * k

    # Conta a ocorrência de cada valor
    for num in v:
        baldes[num] += 1

    # Reconstrói o vetor ordenado
    i = 0
    for j in range(k):
        for _ in range(baldes[j]):
            v[i] = j
            i += 1


def tempo_execucao(arr):
    inicio = time.time()
    
    counting_sort(arr.copy())

    fim = time.time()

    return fim - inicio

sizes = [ 10, 100, 1000, 5000, 10000, 50000, 100000]
for i in range(0, len(sizes)):
    array = np.random.randint(0, 10000, size=sizes[i])
    print(f"Tempo de execução para o array com {sizes[i]} posições: {tempo_execucao(array)}")