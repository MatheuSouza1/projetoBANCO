from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Matheus", "22998662757")
conta = Conta(c1.get_nome(), 1222)

conta.deposito(2000)
conta.extrato()
conta.saque(50)
conta.extrato()