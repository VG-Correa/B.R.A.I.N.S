import os
from statistics import mode
from collections import Counter
    
def Moda(dados=[],biblioteca=False):
    if len(dados) == 0:
        return 0

    if biblioteca:
        frequencia = Counter(dados)
        maximo = max(Counter(dados).values())
        modas = [moda for moda, freq in frequencia.items() if freq == maximo]
        
        if len(modas) == len(dados):
            return "Amodal"

        return str(modas).strip('[]')
    else:
        dados = Ordenar_Crescente(dados)

        items = []

        for item in dados:
            if item in items:
                pass
            else:
                items.append(item)

        dic = {}
        
        for dado in dados:
            if dado not in dic:
                dic[dado] = 1
            else:
                dic[dado] += 1

        mais_frequentes = sorted(dic,key=lambda x: dic[x],reverse=True)
        
        modas = []

        for valor, frquencia in dic.items():
            if frquencia == max(dic.values()):
                modas.append(valor)
            

        return "Amodal" if sum(dic.values()) == len(dic.keys()) else str(modas).strip('[]')


def Ordenar_Crescente(dados):
    dados = sorted(dados,key=lambda x : x,reverse=False)
    return dados

def Ordenar_Decrescente(dados):
    dados = sorted(dados,key=lambda x : x,reverse=True)
    return dados
    

def cls():
    os.system('clear')

# dados = [1,2,3,4,5,6,7,8,9,10] # *********** Para fazer Testes **************

