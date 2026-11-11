from pathlib import Path
diretorio = Path(__file__).resolve().parent
arqMatrizes = diretorio / "Matrizes/Matrizes.txt"

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

#Inicialização das matrizes
matrizA = [[0, 0], [0, 0]]
matrizB = [[0, 0], [0, 0]]
matrizC = [[0, 0], [0, 0]]
matrizD = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizE = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizF = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizG = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matrizH = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

f = open(arqMatrizes, 'r')

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
