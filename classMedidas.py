
# ========================= BIBLIOTECAS ===============================
import numpy as np 

# ======================== IMPORTS LOCAIS =============================
import defs1 as df1
import defs2 as df2
import defs3 as df3
from color import color
from datetime import datetime


# Criando uma classe/objeto para retornar todas as medidas
class Medidas: 
    def __init__(self,dados,biblioteca):
        self.dados = dados
        self.biblioteca = biblioteca
        self.Fonte = ("").upper()
        self.Titulo = ""
        self.media = 0
        self.quartils = [0,0,0]
        self.quartil_1 = self.quartils[0]
        self.quartil_2 = self.quartils[1]
        self.quartil_3 = self.quartils[2]
        self.mediana = self.quartil_2
        self.moda = "Amodal"
        self.arquivo = ''

        if len(self.dados) > 0:
            self.Calcular()

    # Função para salvar o TXT
    def Salvar(self):
        texto = ""
        for text in self.dados:
            texto = texto + str(text) + "\n"
        
        if self.Titulo == "":
            self.Titulo == "Banco de Dados " + str(datetime.now())
        
        with open(self.Titulo+'.txt',"w") as arquivo:
            arquivo.writelines(texto)
            self.arquivo = self.Titulo+'.txt'
            
        self.Calcular()

    # Função para calcular as medidas toda vez q a função for chamada
    def Calcular(self):
        self.media = df1.Media(self.dados, self.biblioteca)
        self.quartils = df2.Quartils(self.dados,self.biblioteca)
        self.quartil_1 = self.quartils[0]
        self.quartil_2 = self.quartils[1]
        self.quartil_3 = self.quartils[2]
        self.mediana = self.quartil_2
        self.moda = str(df3.Moda(self.dados,self.biblioteca)).strip('[]')

    # Função para mostrar o resultado personalizado em forma de tabela colorida
    def Show_Medidas(self, colorido = True):
        div = "="*30
        if colorido:
            return f"""            
{color(self.Titulo, 'verde', negrito=True)[:30]:^45} 
{color(div,'azul',negrito=True)}      
{color('Média: ', 'verde',negrito=True):<30} | {round(self.media,2)}
{color('Mediana: ', 'verde',negrito=True):<30} | {round(self.mediana,2)}
{color('1° Quartil: ', 'verde',negrito=True):<30} | {round(self.quartil_1,2)}
{color('3° Quartil: ', 'verde',negrito=True):<30} | {round(self.quartil_3,2)}
{color('Moda: ', 'verde',negrito=True):<30} | {self.moda}
{color(div,'azul',negrito=True)}
Fonte: {self.Fonte}\n""" 

        # Imprime os resultados em um txt, de forma personalizada em forma de tabela sem cor
        else:   
            div = "="*45
            return f'''
{self.Titulo[:30]:^45}
{div}
{"Média: ":<30} | {round(self.media,2)}
{"Mediana: ":<30} | {round(self.mediana,2)}
{"1° Quartil: ":<30} | {round(self.quartil_1,2)}
{"3° Quartil: ":<30} | {round(self.quartil_3,2)}
{"Moda: ":<30} | {self.moda} 
{div}
Fonte: {self.Fonte}'''