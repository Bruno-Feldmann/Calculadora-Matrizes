def somaMatrizes(matriz1, matriz2):
    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
        matrizresultado = [[0 for i in range(len(matriz1[0]))] for j in range(len(matriz1))]
        for i in range (len(matriz1)):
            for j in range (len(matriz1[i])):
                matrizresultado[i][j] = matriz1[i][j] + matriz2[i][j]
        return matrizresultado
    else:
        print("Erro: Matrizes de ordem diferente")
    
def transportaMatriz(matriz1):
    matrizresultado = [[0 for i in range(len(matriz1[0]))] for j in range(len(matriz1))]

    for i in range (len(matriz1)):
        for j in range (len(matriz1[0])):
            matrizresultado[i][j] = matriz1[j][i]
    return matrizresultado

def multiplicaMatrizes(matriz1, matriz2):
    if len(matriz1) == len(matriz2[0]):
        matrizresultado = [[0 for i in range(len(matriz1[0]))] for j in range(len(matriz1))]
        for i in range(len(matriz1)):
            for j in range(len(matriz1)):
                produto = 0
                for k in range(len(matriz1)):
                    produto += matriz1[j][k] * matriz2[k][i]
                matrizresultado[j][i] = produto
        return matrizresultado
    else:
        print("Erro: número de colunas da primeira matriz é diferente do número de linhas da segunda")