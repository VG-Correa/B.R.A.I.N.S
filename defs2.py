import numpy as np
dados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# dados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# dados = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
# dados = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210]

def Quartils(dados,biblioteca):
    if len(dados) == 0:
        return [0,0,0]
    dados = sorted(dados)
    # Função para calcular o 1º, 2º e 3º quartil - criada pelos desenvolvedores
    if not(biblioteca):
        tamanho = len(dados)
        soma = 0
        for i in dados:
            soma += i
        quartil1 = (soma/tamanho)*0.5
        quartil2 = (soma/tamanho)
        quartil3 = ((soma/tamanho)*0.5)*3
        # print("Sem biblioteca")
        
    # Função para calcular o 1º, 2º e 3º quartil - usando biblioteca numpy
    else:
        # Calcula o primeiro quartil
        quartil1 = np.percentile(dados, 25)

        # Calcula o segundo quartil
        quartil2 = np.percentile(dados, 50)

        # Calcula o terceiro quartil 
        quartil3 = np.percentile(dados, 75)
        # print("Com biblioteca")
    
    return [quartil1,quartil2,quartil3]
   
# print(Quartils(dados,biblioteca=True))
# print(30*"=")
# print(Quartils(dados,biblioteca=False))
