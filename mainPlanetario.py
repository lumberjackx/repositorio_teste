#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MSI
#
# Created:     23/06/2022
# Copyright:   (c) MSI 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
import turtle as t

class sistemaPlanetario:                    #Classe mae que contem o dicio_sistema
    dicio_sistema = {"Poeira Interestelar" : "são pequenos grãos de poeiras com dimensões da ordem de um décimo de mícron responsáveis pela elevada obscuridade observada na direção das protoestrelas.",
        "Satelites Naturais" : "Um satélite natural é um corpo celeste que orbita em torno de um planeta ou outro corpo maior.", "Asteroides" : "são corpos rochosos de estrutura metálica que orbitam em torno do sol como os planetas.",
        "Planeta" : "é um corpo celeste que orbita uma estrela ou um remanescente de estrela, com massa suficiente para se tornar esférico pela sua própria gravidade.", "Meteoro" : "também conhecido por Estrela Cadente é um fenômeno astronômico da passagem de um objeto sólido pela atmosfera terrestre, proveniente do espaço.",
        "Cometa" : "é um pequeno corpo gelado do Sistema Solar que, ao passar perto do Sol, aquece e começa a liberar gases, processo que é chamado de desgaseificação."}

class sistemaSolar(sistemaPlanetario):      #Classe herdada de sistemaPlanetario que contem uma lista planetas
    planetas = ["Mercurio", "Venus", "Terra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno", "Plutao"]

class planeta(sistemaSolar):                #Classe herdade de sistemaSolar que contem os atributos de um planeta
    proximidade_sol = None
    existencia_vida = None
    quantidade_agua = 0
    ponto_mais_alto = None

def funcao_opcao1():                        #Impressao das chaves do objeto dicio e procura o significado da chave escolhida

    dicio = sistemaPlanetario()             #criacao do objeto dicio que e uma instancia da classe sistemaPlanetario

    for chave in dicio.dicio_sistema:       #imprime as chaves do dicionario dicio_sistema
        print("\t", chave)
    escolha = input("Escolha um dos termos para descobrir o significado: ")
    try:                                                                        #try and catch para validacao das chaves do dicionario ou seja da escolha escolhida
        print("\n\t %s -> %s\n" %(escolha.upper(), dicio.dicio_sistema[escolha]))
    except KeyError:
        print("\nEntrada incorreta, ou mal escrita\n")

    input("Prima ENTER para continuar...\n")

def funcao_opcao2(sistema_solar):                    #Impressao da lista planetas atraves de um objeto instanciado pela classe sistemaSolar

    for planeta in sistema_solar.planetas:
        print("\t", planeta)

    input("Prima ENTER para continuar...\n")

def funcao_opcao3(array_planetas, sistema_solar):       #Menu secundario que permite inserir info sobre os planetas ou ver as info sobre eles
    opcao = 0
    while(opcao != 3):
        print("1 - Inserir informaçoes sobre planeta")
        print("2 - Ver informacoes sobre planeta")
        print("3 - Voltar ao menu principal")
        print()
        opcao = int(input("Qual a opcao que deseja: "))
        if(opcao == 1):
            inserir_info(array_planetas, sistema_solar)
        elif(opcao == 2):
            ver_planeta(array_planetas, sistema_solar)
        elif(opcao == 3):
            print()
        else:
            print("\nOpcao Invalida\n")

def inserir_info(array_planetas, sistema_solar):        #Funcao que me permite adicionar informacoes sobre um planeta escolhido

    for i in range(len(sistema_solar.planetas)):
        print("%d - %s" %(i+1, sistema_solar.planetas[i]))
    print()
    opcao = int(input("Qual planeta deseja fazer alteracoes: "))

    try:                                                #try and catch para validacao dos atributos de um planeta e validacao da opcao escolhida
        array_planetas[opcao-1].proximidade_sol = input("Qual a proximidade ao sol: ")
        array_planetas[opcao-1].existencia_vida = input("Existencia de vida? [True | False]: ")
        array_planetas[opcao-1].quantidade_agua = float(input("Quantidade de agua: "))
        array_planetas[opcao-1].ponto_mais_alto = input("Qual o ponto mais alto: ")
        print("\nInformacoes Adicionadas com SUCESSO\n")
    except ValueError:
        print("\nEntrada incorreta\n")
    except IndexError:
        print("\nNumero do planeta escolhido invalido\n")

    input("Prima ENTER para continuar...\n")

def ver_planeta(array_planetas, sistema_solar):     #Funcao que me permite ver as informacoes sobre um planeta escolhido

    for i in range(len(sistema_solar.planetas)):
        print("%d - %s" %(i+1, sistema_solar.planetas[i]))
    print()
    opcao = int(input("Qual planeta deseja ver: "))
    try:                                            #try and catch para validacao da variavel opcao
        print("\n-------%s-------\n" %(sistema_solar.planetas[opcao-1]))
        print("Proximidade do sol -> %s" %(array_planetas[opcao-1].proximidade_sol))
        print("Existencia de vida -> %s" %(array_planetas[opcao-1].existencia_vida))
        print("Quantidade de agua -> %.1f%%" %(array_planetas[opcao-1].quantidade_agua))
        print("Ponto mais alto -> %s\n" %(array_planetas[opcao-1].ponto_mais_alto))
    except IndexError:
        print("\nNumero do planeta escolhido invalido\n")

    input("Prima ENTER para continuar...\n")

def funcao_opcao4(array_planetas, sistema_solar):   #Funcao que adiciona a lista sistema_solar.planetas e ao array_planetas o planeta Psiuno

    for planet in sistema_solar.planetas:           #Se ja tiver sido inserido alguma vez ele entra aqui e nao deixa criar novamente Psiuno
        if(planet == "Psiuno"):
            print("\nDesculpe o planeta Psiuno ja foi adicionado, nao pode adicionar outra vez, esta disponivel no menu 3, obrigado\n")
            return

    print("\nDescobrimos um novo planeta de seu nome Psiuno, Aguarde enquanto fazemos as alteraçoes necessarias...")
    time.sleep(5)
    check = 0
    while(check != 1):                          #ciclo para validacao da posicao, so sai se o check vier a 1
        print("\n1 - Primeira posicao")
        print("2 - Segunda posicao")
        print("3 - Terceira posicao")
        print("4 - Quarta posicao")
        print("5 - Quinta posicao")
        print("6 - Sexta posicao")
        print("7 - Setima posicao")
        print("8 - Oitava posicao")
        print("9 - Nona posicao")
        print("10 - Decima posicao\n")
        posicao = int(input("Em que posicao quer colocar Psiuno: "))    #Pergunta que posicao quer que Psiuno tenha
        if(posicao >= 1 and posicao <= 10):
            print("Adicionando Psiuno a lista planetas, aguarde...")
            time.sleep(3)
            sistema_solar.planetas.insert(posicao-1, "Psiuno")              #Insere o planeta Psiuno na lista sistema_solar.planetas na posicao desejada
            print("Adicionando ao array planetas o objecto Psiuno, aguarde...")
            time.sleep(3)
            Psiuno = planeta()                                              #Criacao do objeto Psiuno que e um planeta
            array_planetas.insert(posicao-1, Psiuno)                        #Insere o objeto planeta Psiuno no array_planetas na posicao desejada
            print("Planeta Psiuno adicionado com SUCESSO, agora ja esta disponivel no menu 2, no menu 3 e no menu 5...")
            check = 1
        else:
            print("\nNumero da posicao escolhido invalido, escolha outro\n")


    input("Prima ENTER para continuar...\n")

def funcao_opcao5(sistema_solar):       #Funcao que desenha o sistema solar no turtle

    t.reset()
    screen = t.Screen()
    screen.bgcolor("black")

    t.penup()                   #Inicia desenho do sol
    t.goto(0,-25)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(25)
    t.end_fill()                #termina desenho do sol

    distancia_sol = 25          #Incializacao da variavel distancia_sol

    for planeta in sistema_solar.planetas:  #Roda a lista sistema_solar.planetas em busca das caracteristicas de cada planeta para depois se chamar o desenhar_planeta
        if(planeta == "Mercurio"):
            raio = 10
            desenhar_planeta(distancia_sol+raio+10,-raio,raio, "red")   #funcao que me desenha um planeta dadas as caracteristicas dele, distancia ao sol , raio e cor...
        elif(planeta == "Venus"):
            raio = 10
            desenhar_planeta(distancia_sol+raio+10,-raio,raio,"orange")
        elif(planeta == "Terra"):
            raio = 15
            desenhar_planeta(distancia_sol+raio+10,-raio,raio,"blue")
        elif(planeta == "Marte"):
            raio = 15
            desenhar_planeta(distancia_sol+raio+10,-raio,raio,"DarkRed")
        elif(planeta == "Jupiter"):
            raio = 50
            desenhar_planeta(distancia_sol+raio+10,-raio,raio,"orange")
        elif(planeta == "Saturno"):
            raio = 40
            desenhar_planeta(distancia_sol+raio+10,-raio,raio,"gold")
        elif(planeta == "Urano"):
            raio = 20
            desenhar_planeta(distancia_sol+raio+10,-raio,raio,"green")
        elif(planeta == "Neptuno"):
            raio = 20
            desenhar_planeta(distancia_sol+raio+10,-raio,raio,"cyan")
        elif(planeta == "Plutao"):
            raio = 10
            desenhar_planeta(distancia_sol+raio+10,-raio,raio,"white")
        else:                                                           #Este else e para o planeta Psiuno se este ja tiver sido criado senao nao entra aqui, e se ele entrar aqui o planeta Psiuno
            raio = 15                                                   #e adicionado ao esquema conforme a posicao escolhida no menu 4
            desenhar_planeta(distancia_sol+raio+10,-raio,raio,"purple")
            print("\nATENCAO!! PSIUNO esta de cor roxa\n")

        distancia_sol = distancia_sol + 2*raio + 10                     #Equacao que me permite obter a nova distancia ao sol(Ou seja da-me a cordenada no eixo do x para saber onde devo começar a
                                                                        #desenhar o proximo planeta)
def desenhar_planeta(cordenada_x, cordenada_y, raio, cor):              #funcao que me desenha o planeta dadas as caracteristcas do planeta. ex: distancia ao sol(que sao dadas pelo cordenada_x e pela
    t.penup()                                                           #cordenada_y) raio e cor
    t.goto(cordenada_x, cordenada_y)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

def main():                                                 #MAIN
    pass

if __name__ == '__main__':
    main()

Mercurio = planeta()                                        #Criacao dos objetos do tipo planeta() e definir caracteristicas do objeto planeta Terra
Venus = planeta()
Terra = planeta()
Terra.proximidade_sol = "3 # Referindo-se ao 3º planeta a contar a partir do sol"
Terra.existencia_vida = True
Terra.quantidade_agua = 70.5
Terra.ponto_mais_alto = "Monte Everest"
Marte = planeta()
Jupiter = planeta()
Saturno = planeta()
Urano = planeta()
Neptuno = planeta()
Plutao = planeta()

array_planetas = [Mercurio, Venus, Terra, Marte, Jupiter, Saturno, Urano, Neptuno, Plutao]          #Insercao dos objetos do tipo planeta() dentro de um array

sistema_solar = sistemaSolar()                                                          #Criacao de um objeto sistema_solar que e uma instancia da classe SistemaSolar() e que contem a lista de planetas

opcao = 0
while(opcao != 6):
    print("-------Menu-------")                                                 #MENU
    print("1 - Dicionarios")
    print("2 - Listar Planetas")
    print("3 - Info sobre Planetas")
    print("4 - Descobrir um novo planeta Psiuno")
    print("5 - Desenhar sistema solar no turtle")
    print("6 - Sair")
    print()
    opcao = int(input("Qual a opcao que deseja: "))

    if(opcao == 1):
        funcao_opcao1()
    elif(opcao == 2):
        funcao_opcao2(sistema_solar)
    elif(opcao == 3):
        funcao_opcao3(array_planetas, sistema_solar)
    elif(opcao == 4):
        funcao_opcao4(array_planetas, sistema_solar)
    elif(opcao == 5):
        funcao_opcao5(sistema_solar)
    elif(opcao == 6):
        print("\nObrigado por nos consultar, bye bye!")
    else:
        print("\nOpcao Invalida\n")
