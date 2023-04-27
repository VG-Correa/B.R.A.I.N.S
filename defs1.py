dados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

import statistics
import os
import sys
import platform

def cls():
    if platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('cls')

def Media(dados,biblioteca):
    if len(dados) == 0:
        return 0
        
    # Função para calcular a Média - criada pelos desenvolvedores
    if not(biblioteca):
        media = sum(dados) / len(dados)
        
    else:
    # Função para calcula Média - Com Biblioteca
        media = statistics.mean(dados)
            
    return media


#def Mostrar_dados(dados, separador=","):

    #for valor in dados:
        #print(valor, end="")

        #if dados < len(dados) - 1:
            #print(separador, end="")
        #if (valor+1) % 10 == 0:
            #print("\n")
    
    

    #dados_str = separador.join(str(valor) for valor in dados):

    #print(formato.format(valor), end="")

    #for valor in dados:
        #print(valor, end="")
        #if valor < len(dados):
            #print(separador, end="")

        #if (valor) % 10 == 0:
            #print("\n") 



#Mostrar_dados(dados, ",")


# maximo = max(dados)
# tamanho = len(str(maximo))

# # print(tamanho)

# for i in dados:
#     print(f'{i:<{tamanho}} |',sep="")
    
# 1     2     3     4     5     6     7     8     9     10
# 11    12    13    14    15    16    17    18    19    20
# 21    22    23    24    25    26    27    28    29    30
# 1000



     