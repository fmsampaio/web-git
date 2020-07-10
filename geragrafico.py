from leitorarquivo import LeitorArquivo

import numpy as np
import matplotlib.pyplot as plt

def main():
    leitor = LeitorArquivo("data.txt")
    valores = leitor.getValores()
    print(valores)

    plt.xlabel('Amostragem')
    plt.ylabel('Valores de entrada')
    
    for i in range(len(valores)):
        plt.plot(valores[i], label='Série ' + str(i+1))
    
    plt.title('Gráfico de linhas')
    plt.legend(loc='upper left')
    plt.show()

main()
