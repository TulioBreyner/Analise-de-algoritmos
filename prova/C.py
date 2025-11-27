def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def ordena(lista):
    impares = []
    pares = []
    for i in lista:
        if i%2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    impares = merge_sort(impares)
    pares =merge_sort(pares)

    return impares+pares    


N = int(input())
lista = [int(x) for x in input().split()]
lista_ordenada = ordena(lista)
for i in lista_ordenada:
    print(i, end=" ")