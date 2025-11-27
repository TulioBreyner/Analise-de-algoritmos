def distancia_quadrado(x, y):
    return x*x + y*y

def ordenar_pontos_por_distancia(coord_list):
    if not coord_list:
        return ["Erro: Entrada de pontos vazia."]
    
    pontos = []
    
    for linha in coord_list:
        x_str, y_str = linha.split()
        x = int(x_str)
        y = int(y_str)
        pontos.append((x, y))

    pontos_ordenados = sorted(pontos, key=lambda ponto: distancia_quadrado(ponto[0], ponto[1]))
    
    saida_formatada = [f"{x} {y}" for x, y in pontos_ordenados]
            
    return saida_formatada


N = int(input())
coord_list = []
for i in range(N):
    coord = input().strip()
    coord_list.append(coord)

resultados = ordenar_pontos_por_distancia(coord_list)

for linha in resultados:
    print(linha)