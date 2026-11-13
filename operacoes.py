def imprimirMatrizes(matriz):
    print()
    for j in range(len(matriz)):
        print(matriz[j])
    print()

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


            somaPositivos += produtoPositivos
            somaNegativos += produtoNegativos

    
        return somaPositivos - somaNegativos

    if len(matriz1) == 4: # Para matrizes 4x4
        matrizCofator1 = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        matrizCofator2 = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        matrizCofator3 = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        matrizCofator4 = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        contador1 = 0
        contador2 = 0  
        contador3 = 0
        contador4 = 0

        for i in range(1, 4, 1):
            for j in range(len(matriz1)):
                if j != 3:
                    matrizCofator1[i- 1][contador1] = matriz1[i][j]
                    contador1 = (contador1 + 1) % 3
                if j != 2:
                    matrizCofator2[i - 1][contador2] = matriz1[i][j]
                    contador2 = (contador2 + 1) % 3
                if j != 1:
                    matrizCofator3[i - 1][contador3] = matriz1[i][j]
                    contador3 = (contador3 + 1) % 3
                if j != 0:
                    matrizCofator4[i - 1][contador4] = matriz1[i][j]
                    contador4 = (contador4 + 1) % 3    

        print(determinanteMatriz(matrizCofator1))
        print(determinanteMatriz(matrizCofator2))
        print(determinanteMatriz(matrizCofator3))
        print(determinanteMatriz(matrizCofator4))

        cofator1 = ((-1) ** 5) *  determinanteMatriz(matrizCofator1)
        cofator2 = ((-1) ** 4) *  determinanteMatriz(matrizCofator2)
        cofator3 = ((-1) ** 3) *  determinanteMatriz(matrizCofator3)
        cofator4 = ((-1) ** 2) *  determinanteMatriz(matrizCofator4)

        print(cofator1, cofator2, cofator3, cofator4)

        determinante = matriz1[0][0] * cofator4
        determinante += matriz1[0][1] * cofator3
        determinante += matriz1[0][2] * cofator2
        determinante += matriz1[0][3] * cofator1

        return determinante