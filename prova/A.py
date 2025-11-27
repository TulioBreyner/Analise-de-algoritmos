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

def busca_binaria(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        if x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

mapeados = [int(x) for x in input().split()]
buscar = [int(x) for x in input().split()]

mapeados = merge_sort(mapeados)

for local in buscar:
    if busca_binaria(mapeados, local):
        print(f'{local} Está mapeado')
    else:
        print(f'{local} Não está mapeado')
    