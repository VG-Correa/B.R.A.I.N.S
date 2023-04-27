import Menu_seleção
from menu import *
import os
import time                     # Biblioteca time que fornece várias funções relacionadas ao tempo
from classMedidas import *      # *Importando todas as funções da classe "Medidas"
from color import color         # Importa a função color do arquivo color.py
import sys
import platform


# Função sleep que recebe uma mensagem e um tempo em segundos
def sleep(mensagem,tempo):

    while tempo > 0:
        cls()
        print(mensagem,"...",tempo)
        tempo -= 1
        time.sleep(0.5)
        cls()

# Função cls que limpa a tela do terminal
def cls():
    if platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('cls')

# A classe MENU possui um construtor __init__() que define os atributos
class Menu:
    def __init__(self,biblioteca=False):
        self.nome_cliente = ""
        self.cabeçalho = """\033[36m
██████╗    ██████╗     █████╗    ██╗   ███╗   ██╗   ███████╗
██╔══██╗   ██╔══██╗   ██╔══██╗   ██║   ████╗  ██║   ██╔════╝
██████╔╝   ██████╔╝   ███████║   ██║   ██╔██╗ ██║   ███████╗
██╔══██╗   ██╔══██╗   ██╔══██║   ██║   ██║╚██╗██║   ╚════██║
██████╔╝██╗██║  ██║██╗██║  ██║██╗██║██╗██║ ╚████║██╗███████║
╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚══════╝\033[0;0m
\033[34mBrilliantly Robust Analysis and Intelligence Network System\033[0;0m"""
        
        self.FATEC = """
███████╗ █████╗ ████████╗███████╗ ██████╗       
██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝       
█████╗  ███████║   ██║   █████╗  ██║            
██╔══╝  ██╔══██║   ██║   ██╔══╝  ██║            
██║     ██║  ██║   ██║   ███████╗╚██████╗       
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝       
                                                
███████╗███████╗██████╗ ██████╗  █████╗ ███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══███╔╝
█████╗  █████╗  ██████╔╝██████╔╝███████║  ███╔╝ 
██╔══╝  ██╔══╝  ██╔══██╗██╔══██╗██╔══██║ ███╔╝  
██║     ███████╗██║  ██║██║  ██║██║  ██║███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
Professor: Luis Carlos dos Santos Filho
Disciplina: Estatística"""
                                                
        self.programadores = """ 
█████╗ ██╗   ██╗██████╗ ██████╗ ███████╗██╗   ██╗    ██████╗    
██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔════╝╚██╗ ██╔╝    ██╔══██╗   
███████║██║   ██║██║  ██║██████╔╝█████╗   ╚████╔╝     ██████╔╝   
██╔══██║██║   ██║██║  ██║██╔══██╗██╔══╝    ╚██╔╝      ██╔══██╗   
██║  ██║╚██████╔╝██████╔╝██║  ██║███████╗   ██║       ██████╔╝██╗
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═════╝ ╚═╝
                                                                 
 ██████╗ █████╗ ██╗ ██████╗     ██████╗                          
██╔════╝██╔══██╗██║██╔═══██╗    ██╔══██╗                         
██║     ███████║██║██║   ██║    ██████╔╝                         
██║     ██╔══██║██║██║   ██║    ██╔══██╗                         
╚██████╗██║  ██║██║╚██████╔╝    ██████╔╝██╗                      
 ╚═════╝╚═╝  ╚═╝╚═╝ ╚═════╝     ╚═════╝ ╚═╝                      
                                                                 
██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗      ██████╗       
██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗    ██╔════╝       
██║   ██║██║██║        ██║   ██║   ██║██████╔╝    ██║            
╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗    ██║            
 ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║    ╚██████╗██╗    
  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝"""

        self.dados = Medidas    
        self.biblioteca = biblioteca
        self.select = Menu_seleção.Menu_seleção(cabeçalho=self.cabeçalho)

    # Função de Tela de Apresentação
    def Tela_Apresentação(self):
        cabeçalho = self.FATEC

        self.select.options(cabeçalho=cabeçalho,opções=["Continuar..."])
        self.select.options(cabeçalho="Programadores: \n" + self.programadores,opções=["Continuar..."])
        self.Tela_Intro()

    # Função que apresenta um menu com opções para selecionar ou criar bancos de dados.
    def Tela_Intro(self):
        if self.nome_cliente == "":
            descrição = "\nMuito bem vindo ao nosso sistema, quer informar seu nome ?"
            
            opt = ["Informar meu nome","Continuar como anônimo","Sair"]

            opt = self.select.options(descrição=descrição,opções=opt)

            if opt == 2:
                self.Exit()
            elif opt == 1:
                self.nome_cliente = "Usuário"
            elif opt == 0:
                self.set_nome_usuario()

        descrição = f"Olá, {self.nome_cliente}\nO que deseja fazer:"

        opt = ["Selecionar Banco de Dados","Criar Banco de Dados","Voltar do início","Sair"]
        opt = self.select.options(descrição=descrição,opções=opt)
        
        if opt == 0: # Seleciona o banco de dados
            self.Tela_Selecionar_banco_de_dados()

        elif opt == 1: # Cria um banco de dados do zero
            self.Tela_Criar_Banco_dados()
            self.Tela_Intro()

        elif opt == 2: # Retorna a apresentação
            self.Tela_Apresentação()

        elif opt == 3: # Encerra o programa
            self.Exit()
            
    # Menu > Selecione banco de dados
    def Tela_Selecionar_banco_de_dados(self):
        cls()

        opt = self.Get_ArquivosNoDiretorio() + ['Voltar']
        opt = opt[self.select.options(descrição="Selecione o banco de dados:", opções=opt)]
        
        try:
            cls()
            with open(opt,'r') as dados:
                
                dados = [float(dado.rstrip()) for dado in dados.readlines()]
          
                self.dados = Medidas(dados,self.biblioteca)
                self.dados.arquivo = opt
                opt = opt.strip(".txt")
                titulo = input(self.cabeçalho + f"\n\n\nInsira o título do seu relatório de dados ou apenas enter para manter {opt}: \n").upper()

                if titulo == "":
                    titulo = opt.strip(".txt")

                self.dados.Titulo = titulo
                
                cls()
                self.dados.Fonte = input(self.cabeçalho + "\n\n\nInsira a fonte dos dados:\n")
                cls()

        except:
            if opt == "Voltar":
                self.Tela_Intro()
            else:
                sleep("Banco de dados não aceito",5)
                self.Tela_Selecionar_banco_de_dados()
        cls()
        self.Tela_opções_dados()

    def Tela_opções_dados(self):
        cls()
        descrição = f"Área do Banco de dados: {self.dados.Titulo}\n\nSelecione a opção desejada:"
        opt = ["Mostrar Dados","Medidas Gerais","Baixar Resultados","Histograma","Editar Banco de dados","Voltar"]
        opt = self.select.options(descrição=descrição,opções=opt)

        if opt == 0: # Mostrar Dados
            self.Mostrar_dados()
            self.Tela_opções_dados()
            
        elif opt == 1: # Medidas Gerals
            cls()
            print(self.cabeçalho)
            print(self.dados.Show_Medidas())
            print("\nPressione Enter para continuar...")
            input()
            
            # Função da classe Medidas para mostrar os dados de forma organizada
            self.Tela_opções_dados()

        elif opt == 2: # Baixa os resultados
            cls()
            print(self.cabeçalho + "\n")
            nome_arquivo = input("Qual o nome do arquivo que deseja salvar:\n").strip('.txt') + ".txt"

            dados = self.dados.Show_Medidas(colorido=False)
            novo_arquivo = open(nome_arquivo,'w')
            novo_arquivo.writelines(dados)

            novo_arquivo.close()
            sleep(f"Arquvio {nome_arquivo} criado com sucesso",10)
            self.Tela_opções_dados()

        elif opt == 3:  # Histograma
            sleep("Em processo de Implementação...",5)
            self.Tela_opções_dados()

        elif opt == 4:  # Editar Banco de dados
            self.Tela_Editar_Banco_Dados()

        elif opt == 5: # Voltar
            self.Tela_Selecionar_banco_de_dados()

    # Busca de arquivos no Diretório
    def Get_ArquivosNoDiretorio(self) -> list:
        diretorio = os.getcwd()
        lista_arquivos = os.listdir(diretorio)
        lista_arquivos = [arquivo for arquivo in lista_arquivos if arquivo.endswith('.txt')]
        return lista_arquivos

    # Função para inserir nome do usuário e validar o mesmo
    def set_nome_usuario(self):
        self.nome_cliente = input(self.cabeçalho + "\n\n\n Digite seu nome:\n\n")
        descrição = f"\n\n\nSeu nome é: {self.nome_cliente}?"
        opt = ["Sim","Corrigir","Sair"]
        opt = self.select.options(descrição=descrição,opções=opt)
        cls()
        if opt == 2:
            self.Exit()
        elif opt == 1:
            self.set_nome_usuario()
        else:
            return 0

    # Função para o usuário criar seu próprio banco de dados
    def Tela_Criar_Banco_dados(self):
        cls()
        while True:
            cabeçalho = self.cabeçalho + "\n\n\nPara criar um novo banco de dados, por favor, insira o nome do banco:\n"
            titulo =  input(cabeçalho).upper()
            if titulo == "":
                sleep(self.cabeçalho + "\n\n\nO Banco precisa de um nome!!",5)
                continue
            else:
                break

        Novo_Banco = Medidas([],biblioteca=self.biblioteca)
        Novo_Banco.Titulo = titulo
        Novo_Banco.Titulo = Novo_Banco.Titulo.strip(".txt")
        Novo_Banco.arquivo = Novo_Banco.Titulo + '.txt'
        cls()
        cabeçalho = self.cabeçalho + "\n\n\nAgora insira a Fonte dos dados:\n"
        Novo_Banco.Fonte = input(cabeçalho).upper()
        self.dados = Novo_Banco

        with open(self.dados.arquivo,'w') as arquivo:
            pass            
        self.Tela_opções_dados()

    # Função para Editar banco de dados
    def Tela_Editar_Banco_Dados(self):
        descrição = f"Tela de edição de dados\nBanco: {self.dados.Titulo}\n\nSelecione a opção desejada:"

        opt = ["Mostrar dados","Adicionar Dados","Excluir Dados", "Alterar Título ou Fonte","Salvar como","Apagar Banco de dados","Voltar"]
        opt = self.select.options(descrição=descrição,opções=opt)
        
        if opt == 0: # Mostrar dados
            self.Mostrar_dados()
            self.Tela_Editar_Banco_Dados()

        elif opt == 1: # Adicionar Dados
            self.Adicionar_dados()       
            self.Tela_Editar_Banco_Dados()

        elif opt == 2: # Excluir Dados
            self.Excluir_dados()
            self.Tela_Editar_Banco_Dados()

        elif opt == 3: # Alterar Título ou Fonte
            self.Alterar_Titulo() 
            self.Tela_Editar_Banco_Dados()
            
        elif opt == 4: # Salvar       
            self.Salvar_como()
            self.Tela_Editar_Banco_Dados()

        elif opt == 5: # Apagar Banco de dados
            self.Excluir_Banco()
            self.Tela_Intro()
            
        elif opt == 6: # Voltar
            self.Tela_opções_dados()

    # Adicionar dados no banco de dados e fazer verificação se são caracteres numéricos
    def Adicionar_dados(self):
        resp = ""
        while not resp.isalpha():
            cls()
            print(self.cabeçalho + "\n\n\nDigite o próximo valor em seguida aperte ENTER para continuar... OU pressione qualquer letra para sair: ")
            resp = input()

            if resp.isalpha() or resp == "":
                break
            self.dados.dados.append(int(resp))
            self.dados.Salvar() 

    # Função para alterar o título do banco de dados
    def Alterar_Titulo(self):
        cls()
        self.dados.Titulo = input(self.cabeçalho + "\n\n\nInsira o título dos dados: \n ").upper()
        cls()
        self.dados.Fonte = input(self.cabeçalho + "\n\n\nInsira a fonte dos seus dados: \n ")
        cls()
        sleep(self.cabeçalho + "\n\n\nDados alterados com sucesso!",5)   

    # Função para o usuário salvar o resultado das medidas gerais em um TXT
    def Salvar_como(self):
        cls()

        cabeçalho = self.cabeçalho + "\n\n\nQual o nome do novo arquivo que deseja salvar ou deixe VAZIO para cancelar: "
        titulo = input(cabeçalho)

        if not(titulo == ""):    
            self.dados.Titulo = titulo.strip('.txt')
            self.dados.Salvar()

    # Função para excluir itens individualmente, um a um, que estão dentro do banco de dados
    def Excluir_dados(self):        
        cabeçalho = self.cabeçalho + "\n\n\nSelecione o dado a ser excluído:"
        item_excluido = ""

        while True:
            opt = ['Voltar'] +  self.dados.dados
            opt = self.select.options(opções=opt)

            if opt == 0:
                break

            item_excluido = self.dados.dados[opt-1]
            cabeçalho = cabeçalho + f"\nDado {self.dados.dados[opt-1]} foi excluído com sucesso"
            self.dados.dados.pop(opt-1)
            self.dados.Salvar()

    # Função para exibir os dados personalizados para o usuário
    def Mostrar_dados(self):
        cls()
        if len(self.dados.dados) == 0:
            cabeçalho = self.cabeçalho + '\n\n\nO banco não possui informação para mostrar!!\n\nVoltando ao menu anterior'
            sleep(cabeçalho,5)
            return False

        cabeçalho = self.cabeçalho + f'\n\n\nDados do banco: {self.dados.Titulo}\n\n'
        print(cabeçalho)
        dados = self.dados.dados
        maior = len(str(max(dados))) + 2
        limite = 10
        for index, numero in enumerate(dados):
            if index+1 <= limite:
                print(f'{numero:^{maior}}',end='|')
            else:
                # print('a')
                print('')
                limite += 10
                print(f'{numero:^{maior}}',end='|')        
        input()

    # Função para excluir o banco de dados que está no diretório
    def Excluir_Banco(self):
        arquivo = self.dados.arquivo
        descrição = f"ATENÇÃO!!\nTem certeza que deseja excluir o banco de dados: {arquivo}?\n"
        
        opt = ['Não','Sim']
        opt = self.select.options(descrição=descrição,opções=opt)
        
        if opt == 1:
            diretorio = os.getcwd()
            caminho = os.path.join(diretorio,arquivo)
            os.remove(caminho)
            sleep(self.cabeçalho+f'\n\n\nBanco {arquivo} excluído com sucesso!',5)
            self.Tela_Intro()
        else:
            self.Tela_Editar_Banco_Dados()

    # Finalização do programa personalizado
    def Exit(self):
        cls()
        sleep(color(f'\n>>> {self.nome_cliente}, Muito obrigado por usar o ','azul',negrito=True) + color('B.R.A.I.N.','verde',negrito=True) + color('!!!','azul',negrito=True),5)
        exit()
            
meu_Menu = Menu()
meu_Menu.Tela_Apresentação()