import os
carros=[]

class Carro:
    nome=""
    potencia=""
    vel_max=0
    ligado=False

    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.vel_max = int(potencia) * 2
        self.ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def info(self):
        print(f"Nome........: {self.nome}")
        print(f"Potência....: {self.potencia}")
        print(f"Vel.Máxima..: {self.vel_max}")
        print(f"Ligado......: {self.ligado}")

def Menu():
    os.System("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 - Sair")
    print(f"Quantidade de Carro {str(len(carros))}")
    opc = input("Digite uma opcao: ")
    return opc

def NovoCarro():
    os.System("cls") or None
    nome = input("Nome do carro: ")
    potencia = input("Potencia do carro: ")
    carro1 = Carro(nome,potencia)
    carros.append(carro1)
    print("Novo carro criado")
    os.System("pause")

def informacoes():
    os.System("cls") or None
    numero = input("Informe o número do carro que deseja ver as informações: ")

    try:
        carros[int(numero)].info()
    except:
        print("Carro não existe na lista")
    os.System("pause")

def excluirCarro():
    os.System("cls") or None
    numero = input("Informe o número do carro que deseja excluir: ")

    try:
        del carros[int(numero)]
    except:
        print("Carro não existe na lista")
    os.System("pause")

def ligarDesligarCarro():
    os.System("cls") or None
    numero = input("Informe o número do carro que deseja ligar: ")

    try:
        carros[int(numero)].liga_desliga()
        carro_status = "ligado" if carros[int(numero)].ligado else "desligado"
        print(f"Carro {carro_status}")
    except:
        print("Carro não existe na lista")
    os.System("pause")

def listarCarro():
    os.System("cls") or None
    p = 0
    for carro in carros:
        print(f"{str(p)} - {carro.nome}")

    os.System("pause")