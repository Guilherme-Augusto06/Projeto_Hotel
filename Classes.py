import os

User_hotel = []
ap_simples = []
ap_simples_casal = []
ap_duplo = []
ap_duplo_casal = []
ap_luxo = []
ap_master = []

class Hotel:
    def __init__(self, nome, estrelas, diaria, qtd_quartos):
        self._nome = nome
        self._diaria = diaria
        self._qtd_quartos = qtd_quartos

class Quartos(Hotel):
    def __init__(self, listar_quartos):
        self._listar_quartos = listar_quartos


class Apartamento_simples(Quartos):
    def __init__(self, ap_simples, ap_simples_casal):
        self._ap_simples = ap_simples
        self._ap_simples_casal = ap_simples_casal

    def ap_simples(self):
        print("""Apartamento Simples
              1 cama de solteiro, 1 banheiro, frigobar, internet, e TV(22 polegadas)
              Valor: R$ 130,00""")
    
    def ap_simples_casal(self):
        print("""Apartamento Simples de Casal
              1 Cama de casal, 1 banheiro, 1 frigobar, internet e TV""")
        

#//////////////////////////////////////////////////////////////////////////////////////
class Apartamento_duplo(Quartos):
    def __init__(self, ap_duplo, ap_duplo_casal):
        self._ap_duplo = ap_duplo
        self._ap_duplo_casal = ap_duplo_casal
        
    def ap_duplo(self):
        print("""Apartamento Duplo
              2 Camas de solteiro, 1 banheiro, 1 frigobar, internet, TV e Ar Condicionado""")
        quest = int(input("Deseja escolher esse quarto? \n1- Sim \n2- Não \n>"))
        if quest == 1:
            ap_duplo.append(self._nome)
            print("Quarto escolhido!")

        if quest == 2:
            os.sytsem("pause")
            os.system("cls")
        
    def ap_duplo_casal(self):
        print("""Apartamento Duplo
              1 Cama de casal (Queen Size), 1 banheiro, 1 frigobar, internet, TV e Ar condicionado""")
        quest = int(input("Deseja escolher esse quarto? \n1- Sim \n2- Não \n>"))
        if quest == 1:
            ap_duplo_casal.append(self._nome)
            print("Quarto escolhido!")

        if quest == 2:
            os.sytsem("pause")
            os.system("cls")


#////////////////////////////////////////////////////////////////////////////////////////////////
class Apartamento_luxo(Quartos):
    def __init__(self, ap_luxo):
        self._ap_luxo = ap_luxo

    def ap_luxo(self):
        print("""
        2 Camas de casal (Queen Size), 2 Banheiro, 1 Geladeira, 1 Suíte, 1 Ar condicionado, 1 Cozinha, Internet""")

class Apartamento_master(Quartos):
    def __init__(self, ap_master):
        self._ap_master = ap_master

    def ap_master(self):
        print("""
              2 Camas de casal(King Size), 2 Banheiros, 1 Suíte, 1 Hidromassagem, 1 Geladeira, 1 Cozinha, Internet, 1 Ar Condicionado""")
#////////////////////////////////////////////////////////////////////////


        
        

  

        
    
    
   
    
