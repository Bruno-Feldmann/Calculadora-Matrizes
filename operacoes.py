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

def determinanteMatriz(matriz1):
    if len(matriz1) == 2: # Para matrizes 2x2
        a = matriz1[0][0]
        a *= matriz1[1][1]
        b = matriz1[1][0]
        b *= matriz1[0][1]
        return a - b

    elif len(matriz1) == 3: #Para matrizes 3x3

        somaPositivos = 0
        somaNegativos = 0

        for i in range(len(matriz1)):

            produtoPositivos = 1
            produtoNegativos = 1

            for j in range(len(matriz1)):

                colunaPositiva = (i + (j)) % len(matriz1)
                colunaNegativa = (i - (j + 1)) % len(matriz1)

                produtoPositivos *= matriz1[j][colunaPositiva]
                produtoNegativos *= matriz1[j][colunaNegativa]
                print(produtoPositivos)
                print(produtoNegativos)

            somaPositivos += produtoPositivos
            somaNegativos += produtoNegativos
            print(somaPositivos)
            print(somaNegativos)
    
        return somaPositivos - somaNegativos

    if len(matriz1) == 4: # Para matrizes 4x4
        matriz1Cofator1, matriz1Cofator2, matriz1Cofator3, matriz1cofator4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        contador1, contador2, contador3, contador4 = 0
        for i in range (len(matriz1)):
            for j in range (len(matriz1Cofator1)):
                if i != 4:
                    matriz1Cofator1[contador4][j] = matriz1[i][j]
                    contador4 += 1
                elif i != 3:
                    matriz1Cofator2[contador3][j] = matriz1[i][j]
                    contador3 += 1
                elif i != 2:
                    matriz1Cofator2[contador2][j] = matriz1[i][j]
                    contador2 += 1
                elif i != 1:
                    matriz1Cofator2[contador1][j] = matriz1[i][j]
                    contador1 += 1

        cofator1 = -1 ** (len(matriz1) + len(matriz1[0])) *  determinanteMatriz(matriz1Cofator)
        cofator2 = -1 ** (len(matriz1) + len(matriz1[0])) *  determinanteMatriz(matriz1Cofator)
        cofator3 = -1 ** (len(matriz1) + len(matriz1[0])) *  determinanteMatriz(matriz1Cofator)
        cofator4 = -1 ** (len(matriz1) + len(matriz1[0])) *  determinanteMatriz(matriz1Cofator)

        a = 0
        for i in range(len(matriz1)):
            a += matriz1[0][i] * cofator

        return a