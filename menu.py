import os
import color as col
import time
import curses
from curses import *
from curses import wrapper
from curses.panel import *
# import log

# Função que recebe um cabeçalho e as opções que o usuário poderá escolher, retornará o index das opções que o usuário selecionou
def options(cabeçalho,opções):
    # Cabeçalho é o texto que o sistema vai printar no console antes de mostrar as opções a ser escolhida
    # Opções é uma [lista] onde cada item é uma opção que o usuário poderá escolher, exemplo:['Logar','Cadastrar-se','Encerrar']

    nop = len(opções)
        # Verifica o tamanho da lista de opções

    select = 0
        # Inicia a seleção das opções pelo index 0

    tamanho = 6
        # Quantidade de opções que vão aparecer no terminal por vez

    # Como o terminal não pode mostrar todas as opções de uma vez, criamos uma sessão que irá navegar na quantidade de opções
    inicio = 0
        # O index da opção que será o primeiro a aparecer
    fim = tamanho
        # O index do último item que poderá aparecer no terminal
    selectedSession = 0
        # O index da sessão que representa a opção selecionada

    # Se o tamanho do limite das opções for maior que a quantidade de opções, o tamanho recebe o tamanho da quantidade de opções e o fim recebe o limite pelo tamanho
    if tamanho > nop-1:
        tamanho = nop-1
        fim = tamanho

    while True:
        opt = []

        for index, item in enumerate(opções):
            
            if index >= inicio and index <= fim:
                opt.append(item)
        
        # log.NewLog('Defs.options',opt)

        # log.NewLog('Defs.options',opt)

        selec = main(cabeçalho,opt,selectedSession)
        #f'\n| {selectedSession} | {select}\n| Inicio: {inicio} | Fim: {fim} | Tamanho: {tamanho}'#
        if selec == 'enter':
            break

        elif selec == 'cima':
            select -= 1
            selectedSession -= 1

            if select < 0:
                select = nop-1
                fim= nop-1
                inicio = fim-tamanho
                selectedSession = tamanho

            elif selectedSession < 0:
                fim -= 1
                inicio -= 1
                selectedSession = 0

        elif selec == 'baixo':
            select += 1
            selectedSession += 1
    
            if select > nop-1:
                select = 0
                selectedSession = 0
                inicio = 0
                fim = tamanho
            
            elif selectedSession > tamanho:
                fim += 1
                inicio += 1
                selectedSession = tamanho

    return select

# Função que cria um terminal em cima do original que vai 'escutar' o teclado e tratar a tecla digitada.
def main(cabeçalho,opções,select):
    os.system('clear')
    # log.NewLog("Defs.main",select)
    heightWindows = cabeçalho.count('\n')+1+len(opções)+500; widthWindows = 500
    stdscr = curses.initscr()
    stdscr = newwin(heightWindows, widthWindows, 0, 0)
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        
    nop = len(opções) 
    curses.curs_set(0)
    
    stdscr.clear()

    stdscr.addstr(cabeçalho)
    
    for i in range(0,nop): 
        if i == nop-1:
            txt = '\n' + str(opções[i]) + '\n'
        else:
            txt = '\n' + str(opções[i])  

        if i == select:
            stdscr.addstr(txt, 256 )
            # stdscr.refresh()
            # log.NewLog("Defs.main",'igual')
            
        else:
            
            stdscr.addstr(txt)
            # stdscr.refresh()
            # log.NewLog("Defs.main",'diferente')
        
    # log.NewLog("Defs.main",txt)  
    stdscr.refresh()  
    
    key = stdscr.getch()
    curses.endwin()

    if key == 65:
        return 'cima'
    if key == 66:
        return 'baixo'
    if key == 10:
        return 'enter'