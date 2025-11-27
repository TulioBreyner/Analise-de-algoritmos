import math

n = int(input())
data = [n, ]
for _ in range(n):
    entrada = int(input())
    data.append(entrada)

t = data[0]

for i in range(t):
    k = data[i+1]
    n = k + math.isqrt(k) 
    
    while True:
        qtd_quadrados = math.isqrt(n)
        novo_n = k + qtd_quadrados
        
        if novo_n == n:
            break
        n = novo_n
        
    print(n)

