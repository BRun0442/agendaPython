# wait screen
import time

# Terminal colors
from pickle import REDUCE

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"



# clear console
import os
def clear():
  time.sleep(1.5)
  os.system('cls' if os.name=='nt' else 'clear')


continueSearch = True

schedule = {
    "lição Emerson": {"dia":26, "mes":9, "detalhes":"fazer agenda em python", "aula":"DS I"},
    "lição APS": {"dia":3, "mes":10, "detalhes":"fazer diagrama de classes e comunicação e tempo", "aula":"APS"},
    "trabalho de artes": {"dia":22, "mes":9, "detalhes":"elaborar uma coreografia", "aula":"artes"},
    "trabalho nodeJs":{"dia":23, "mes":9, "detalhes":"fazer 9 exercícios mexendo com um Json", "aula":"PW II"},
    "prova do alino":{"dia":19, "mes":9, "detalhes":"tipos de manutenção, MTBF, MTTR", "aula":"Organização industrial 4.0"}
}

def programOptions():
    print("\n------------")
    print("| Agenda:  |")
    print("------------\n")

    print("-----------------------------")
    print("| - Continuar = " + CYAN + "1" + RESET + "           |")
    print("| - SAIR = " + CYAN + "2" + RESET + "                |")
    print("-----------------------------\n")

    if input(RED + "Opção: " + RESET) == "1":
        return True
    else:
        return False

def searchType():
    print("\n------------------------------")
    print("| Digite o que você deseja:  |")
    print("------------------------------\n")

    print("--------------------------------------")
    print("| - Pesquisar items da agenda = " + CYAN + "1" + RESET + "    |")
    print("| - Pesquisar palavras na agenda = " + CYAN + "2" + RESET + " |")
    print("--------------------------------------\n")

    lookingFor = input(RED + "Opção: " + RESET)

    if(lookingFor == "1"):
        searchItems()
    elif(lookingFor == "2"):
        searchWord()


def searchWord():
    lookingFor = input(RED + "Digite qual palavra você deseja pesquisar: " + RESET)

    print("Items da agenda em que aparece o que você pesquisou: \n")
    for items, values in schedule.items():
        if lookingFor in items:
            print(items)

        for keys, value in values.items():
            if lookingFor in str(value):
                print(items)


def search():
    print("------------------------")
    print("| " + BOLD + "Opções da agenda:" + RESET + "    |")
    print("------------------------")
    print(CYAN)

    print("------------------------")
    # for keys, values in schedule.items():
    for keys in schedule:
        print("| ", keys)
    print("------------------------")

    return input(RED + "Digite o que você deseja pesquisar: " + RESET)


def searchItems():
    lookingFor = search()

    clear()

    if lookingFor in schedule.keys():

        print("\n------------------------")
        print(BOLD + lookingFor + RESET)
        print("------------------------")

        for items, values in schedule[lookingFor].items():
            print("     " + CYAN + str(items) + ": " + RESET + str(values))
        print("\n")
            
# def continueProgram():   
#     print("\n------------------------------")
#     print("| Deseja prosseguir(Y/N):         |")
#     print("------------------------------\n")

#     step = input(RED + "(Y/N): " + RESET)

#     if step == "Y":
#         clear()
#     else:


def option():
    clear()

    continueSearch = True
    continueSearch = programOptions()

    while continueSearch == True:
        clear()
        searchType()
        time.sleep(10)
        clear()
        continueSearch = programOptions()


option()
# searchWord()

        