def pularlinha(f):
    f.readline()
    f.readline()

def preencherMatriz(matriz):
    pularlinha(f)
    for j in range (len(matriz)):
        atual = f.readline()
        atual_lista = atual.split()
        for i in range (len(atual_lista)):
            matriz[j][i] = float(atual_lista[i])


matrizA = [[0, 0], [0, 0]]
matrizB = [[0, 0], [0, 0]]
matrizC = [[0, 0], [0, 0]]
matrizD = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizE = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizF = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizG = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matrizH = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
i = 0
j = 0
atual = ""
f = open('Calculadora de Matrizes\\Matrizes\\Matrizes.txt', 'r')

#Matrizes 2x2
preencherMatriz(matrizA)
preencherMatriz(matrizB)
preencherMatriz(matrizC)
f.readline()

#Matrizes 3x3
preencherMatriz(matrizD)
preencherMatriz(matrizE)
preencherMatriz(matrizF)
f.readline()

#Matrizes 4x4
preencherMatriz(matrizG)
preencherMatriz(matrizH)


print(matrizA)
print(matrizB)
print(matrizC)
print(matrizD)
print(matrizE)
print(matrizF)
print(matrizG)
print(matrizH)