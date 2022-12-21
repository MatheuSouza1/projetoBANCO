from Cliente import Cliente
from Conta import Conta

print("CRIE SUA CONTA NO BANCO:")
nome = input("Digite seu nome: ")
num = input("Digite seu numero de telefone: ")
cliente = Cliente(nome, num)
conta = Conta(cliente.get_nome(), 1234)

print("Conta criada:")
conta.extrato()

while True:
    print("Digite o numero da ação desejada: \n[1]Ver extrato\n[2]Fazer deposito\n[3]Saque\n[0]Sair")
    r = input("")
    if r == "0":
        break
    elif r == "1":
        conta.extrato()
    elif r == "2":
        dep = float(input("Quanto você quer depositar? "))
        conta.deposito(dep)
    elif r == "3":
        saque = float(input("Quanto você quer sacar? "))
        conta.saque(saque)
    else:
        print("Digite uma opção válida")