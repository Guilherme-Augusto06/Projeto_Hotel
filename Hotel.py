import os
from Classes import*

def cadastro():
    print("Cadastro")
    nome = input("Digite seu nome: ")
    cpf = int(input("Digite seu cpf: "))
    tel = int(input("Digite seu telefone: "))
    cp = Cadastroo()
    cp.cadastro(nome, cpf, tel)
    
    
def apartamento_simples_oo(ap_simples, ap_simples_casal):
    print("Apartamento Simples")
    ap_simples = Apartamento_simples(ap_simples, ap_simples_casal)
    ap_simples.ap_simples(n)
    os.system("pause")
    os.system("cls")
    menu_quartos()

def apartamento_simples_casal_oo(ap_simples_casal):
    print("Apartamento Simples de Casal")
    ap_simples_casal = Apartamento_simples(ap_simples, ap_simples_casal)
    ap_simples_casal.ap_simples_casal()
    os.system("pause")
    os.system("cls")
    menu_quartos()

def apartamento_duplo_oo(ap_duplo):
    print("Apartamento Duplo")
    ap_duplo = Apartamento_duplo(ap_duplo, ap_duplo_casal)
    ap_duplo.ap_duplo()
    os.system("pause")
    os.system("cls")
    menu_quartos()

def apartamento_duplo_casal_oo(ap_duplo_casal):
    print("Apartamento Duplo de Casal")
    ap_duplo_casal = Apartamento_duplo(ap_duplo, ap_duplo_casal)
    ap_duplo_casal.ap_duplo_casal()
    os.system("pause")
    os.system("cls")
    menu_quartos()

def apartamento_luxo_oo(ap_luxo):
    print("Apartamento de Luxo")
    ap_luxo = Apartamento_luxo(ap_luxo)
    ap_luxo.ap_luxo()
    os.system("pause")
    os.system("cls")
    menu_quartos()

def apartamento_master_oo(ap_master):
    print("Apartamento Master")
    ap_master = Apartamento_master(ap_master)
    ap_master.ap_master()
    os.system("pause")
    os.system("cls")
    menu_quartos()


def sair():
    print("Sair")
    main()

def menu_quartos():
    print("Escolha seu quarto:")
    print("1- Apartamento Simples")
    print("2- Apartamento simples de casal")
    print("3- Apartamento duplo")
    print("4- Apartamento duplo de casal")
    print("5- Apartamento de luxo")
    print("6- Apartamento master")
    print("7- Sair")
    op = int(input("Selecione uma opção: "))
    match op:
        case 1:
            apartamento_simples_oo(ap_simples, ap_simples_casal)
            menu_quartos()
        case 2:
            apartamento_simples_casal_oo(ap_simples_casal, ap)
            menu_quartos()
        case 3:
            apartamento_duplo_oo(ap_duplo)
            menu_quartos()
        case 4:
            apartamento_duplo_casal_oo(ap_duplo_casal)
            menu_quartos()
        case 5:
            apartamento_luxo_oo(ap_luxo)
            menu_quartos()
        case 6:
            apartamento_master_oo(ap_master)
            menu_quartos()
        case 7:
            sair()

def main(): # Função principal
    x = 0
    while x == 0: 
        
            print("Bem vindo ao Hotel")
            print("1- Cadastrar")
            print("2- Sair")
            op = int(input("Selecione uma opção: "))
            match op:
                case 1:
                    cadastro()
                    os.system("cls")
                    menu_quartos()
                case 2:
                    x = 1
                    print("Saindo")
                case _:
                    print("Opção invalida")
        
