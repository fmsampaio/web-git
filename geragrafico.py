from leitorarquivo import LeitorArquivo

import numpy as np
import matplotlib.pyplot as plt

def main():
    leitor = LeitorArquivo("data.txt")
    valores = leitor.getValores()
    print(valores)

    plt.xlabel('Amostragem')
    plt.ylabel('Valores de entrada')
    plt.title('Gráfico de linhas')
    plt.plot(valores)
    plt.show()

main()
