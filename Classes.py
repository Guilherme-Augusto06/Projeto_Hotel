import os
from Hotel import *
cadastro = []
ap_simples = []
ap_simples_casal = []
ap_duplo = []
ap_duplo_casal = []
ap_luxo = []
ap_master = []
nome = []

def menu_quartos():
    print("Escolha seu quarto:")
    print("1- Apartamento Simples")
    print("2- Apartamento simples de casal")
    print("3- Apartamento duplo")
    print("4- Apartamento duplo de casal")
    print("5- Apartamento de luxo")
    print("6- Apartamento master")
    print("7- Sair")

class Hotel:
    def __init__(self, nome, diaria, qtd_quartos):
        self._nome = nome
        self._diaria = diaria
        self._qtd_quartos = qtd_quartos
        

class Cadastroo():
    def cadastro(self, nome, cpf, tel):
        self._nome = nome
        self._cpf = cpf
        self._tel = tel 
        nome = input("Digite seu nome: ")
        cpf = int(input("Digite seu cpf: "))
        tel = int(input("Digite seu telefone: "))
        cadastro.append(self._nome)
        os.system("pause")
        os.system("cls")


class Quartos(Hotel):
    def __init__(self, listar_quartos):
        self._listar_quartos = listar_quartos



class Apartamento_simples(Quartos,Cadastroo):
    def __init__(self, ap_simples, ap_simples_casal):
        self._ap_simples = ap_simples
        self._ap_simples_casal = ap_simples_casal
        self._nome = nome
    def ap_simples(self):
        print("""Apartamento Simples
              1 Cama de solteiro, 1 banheiro, 1 frigobar, internet, TV e Ar Condicionado""")
        quest = int(input("Deseja escolher esse quarto? \n1- Sim \n2- Não \n>"))
        if quest == 1:
            ap_simples.append(self._nome)
            print("Quarto escolhido!")

        if quest == 2:
            os.system("pause")
            os.system("cls")
            menu_quartos()
            
        
    def ap_simples_casal(self, nome):
        print("""Apartamento Simples de Casal
              1 Cama de casal (Queen Size), 1 banheiro, 1 frigobar, internet, TV e Ar Condicionado""")
        quest = int(input("Deseja escolher esse quarto? \n1- Sim \n2- Não \n>"))
        if quest == 1:
            ap_simples_casal.append(self._nome)
            print("Quarto escolhido!")

        if quest == 2:
            os.sytsem("pause")
            os.system("cls")
            menu_quartos()
        





#//////////////////////////////////////////////////////////////////////////////////////
class Apartamento_duplo(Quartos, Cadastroo):
    def __init__(self, ap_duplo, ap_duplo_casal):
        self._ap_duplo = ap_duplo
        self._ap_duplo_casal = ap_duplo_casal
        self._nome = nome

    def ap_duplo(self):
        print("""Apartamento Duplo
              2 Camas de solteiro, 1 banheiro, 1 frigobar, internet, TV e Ar Condicionado""")
        quest = int(input("Deseja escolher esse quarto? \n1- Sim \n2- Não \n>"))
        if quest == 1:
            ap_duplo.append(self._nome)
            print("Quarto escolhido!")

        if quest == 2:
            os.system("cls")
            menu_quartos()
            

    def ap_duplo_casal(self):
        print("""Apartamento Duplo de Casal
              2 Camas de casal (Queen Size), 1 banheiro, 1 frigobar, internet, TV e Ar Condicionado""")
        quest = int(input("Deseja escolher esse quarto? \n1- Sim \n2- Não \n>"))
        if quest == 1:
            ap_duplo_casal.append(self._nome)
            print("Quarto escolhido!")

        if quest == 2:
            os.sytsem("pause")
            os.system("cls")
            menu_quartos()

#////////////////////////////////////////////////////////////////////////////////////////////////
class Apartamento_luxo(Quartos, Cadastroo):
    def __init__(self, ap_luxo):
        self._ap_luxo = ap_luxo
        self._nome = nome

    def ap_luxo(self):
        print("""Apartamento de Luxo
              1 Cama de casal (King Size), 1 banheiro, 1 frigobar, internet, TV, 1 Hidromassagem e Ar Condicionado""")
        quest = int(input("Deseja escolher esse quarto? \n1- Sim \n2- Não \n>"))
        if quest == 1:
            ap_duplo_casal.append(self._nome)
            print("Quarto escolhido!")

        if quest == 2:
            os.sytsem("pause")
            os.system("cls")
            menu_quartos()


class Apartamento_master(Quartos, Cadastroo):
    def __init__(self, ap_master):
        self._ap_master = ap_master
        self._nome = nome

    def ap_master(self):
        print("""Apartamento Master
              1 Cama de casal (King Size), 1 banheiro, 1 frigobar, internet, TV, 1 Hidromassagem, 1 sauna e Ar Condicionado""")
        quest = int(input("Deseja escolher esse quarto? \n1- Sim \n2- Não \n>"))
        if quest == 1:
            ap_master.append(self._nome)
            print("Quarto escolhido!")

        if quest == 2:
            os.sytsem("pause")
            os.system("cls")
            menu_quartos()

#////////////////////////////////////////////////////////////////////////


        
        

  

        
    
    
   
    
