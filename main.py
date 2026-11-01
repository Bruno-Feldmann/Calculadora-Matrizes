import leitor

def imprimirMatrizes(matriz):
    print()
    for j in range(len(matriz)):
        print(matriz[j])
    print()

def seletorMatrizes():
    x = input("Nome da matriz para a operação: ")
    if x.capitalize == 'A':
        return leitor.matrizA
    if x.capitalize == 'B':
        return leitor.matrizB
    if x.capitalize == 'C':
        return leitor.matrizC
    if x.capitalize == 'D':
        return leitor.matrizD
    if x.capitalize == 'E':
        return leitor.matrizE
    if x.capitalize == 'F':
        return leitor.matrizF
    if x.capitalize == 'G':
        return leitor.matrizG
    if x.capitalize == 'H':
        return leitor.matrizH

def somarMatrizes(matriz1, matriz2):
    print("")

while True:
    print("=== MENU ===")
    print("1- Listar matrizes")
    print("2- Somar duas matrizes")
    print("3- Calcular a transposta de uma matriz")
    print("4- Multiplicar duas matrizes")
    print("5- Calcular o determinante de uma matriz")
    print("6- Escalonar uma matriz")
    print("0- Sair")
    opcao = int(input("Opção: "))
    if opcao == 1:
        print("Matriz A:")
        imprimirMatrizes(leitor.matrizA)
        print("Matriz B:")
        imprimirMatrizes(leitor.matrizB)
        print("Matriz C:")
        imprimirMatrizes(leitor.matrizC)
        print("Matriz D:")
        imprimirMatrizes(leitor.matrizD)
        print("Matriz E:")
        imprimirMatrizes(leitor.matrizE)
        print("Matriz F:")
        imprimirMatrizes(leitor.matrizF)
        print("Matriz G:")
        imprimirMatrizes(leitor.matrizG)
        print("Matriz H:")
        imprimirMatrizes(leitor.matrizH)

    elif opcao == 2:
        matrizopera1 = seletorMatrizes
        matrizopera2 = seletorMatrizes
        

    elif opcao == 0:
        break

