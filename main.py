import leitor
import operacoes

matrizopera1 = []
matrizopera2 = []

def seletorMatrizes():
    x = input("Nome da matriz para a operação: ")
    if x.capitalize() == 'A':
        return leitor.matrizA
    elif x.capitalize() == 'B':
        return leitor.matrizB
    elif x.capitalize() == 'C':
        return leitor.matrizC
    elif x.capitalize() == 'D':
        return leitor.matrizD
    elif x.capitalize() == 'E':
        return leitor.matrizE
    elif x.capitalize() == 'F':
        return leitor.matrizF
    elif x.capitalize() == 'G':
        return leitor.matrizG
    elif x.capitalize() == 'H':
        return leitor.matrizH
    else:
        print("Nome de matriz inválido")

while True:
    print("=== MENU ===")
    print("1- Listar matrizes")
    print("2- Somar duas matrizes da mesma ordem")
    print("3- Calcular a transposta de uma matriz")
    print("4- Multiplicar duas matrizes")
    print("5- Calcular o determinante de uma matriz")
    print("6- Escalonar uma matriz")
    print("0- Sair")
    opcao = int(input("Opção: "))
    if opcao == 1:
        print("Matriz A:")
        operacoes.imprimirMatrizes(leitor.matrizA)
        print("Matriz B:")
        operacoes.imprimirMatrizes(leitor.matrizB)
        print("Matriz C:")
        operacoes.imprimirMatrizes(leitor.matrizC)
        print("Matriz D:")
        operacoes.imprimirMatrizes(leitor.matrizD)
        print("Matriz E:")
        operacoes.imprimirMatrizes(leitor.matrizE)
        print("Matriz F:")
        operacoes.imprimirMatrizes(leitor.matrizF)
        print("Matriz G:")
        operacoes.imprimirMatrizes(leitor.matrizG)
        print("Matriz H:")
        operacoes.imprimirMatrizes(leitor.matrizH)

    elif opcao == 2:
        matrizopera1 = seletorMatrizes()
        matrizopera2 = seletorMatrizes()
        operacoes.imprimirMatrizes(operacoes.somaMatrizes(matrizopera1, matrizopera2))

    elif opcao == 3:
        matrizopera1 = seletorMatrizes()
        operacoes.imprimirMatrizes(operacoes.transportaMatriz(matrizopera1))

    elif opcao == 4:
        matrizopera1 = seletorMatrizes()
        matrizopera2 = seletorMatrizes()
        operacoes.imprimirMatrizes(operacoes.multiplicaMatrizes(matrizopera1, matrizopera2))

    elif opcao == 5:
        matrizopera1 = seletorMatrizes()
        print(f"Determinante: {operacoes.determinanteMatriz(matrizopera1)}")

    

    elif opcao == 0:
        print("Programa finalizado")
        break

    else:
        print("Opção inválida")

