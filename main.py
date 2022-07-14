from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

b = Banco()

cl1 = Cliente('Luiz', 30)
cl2 = Cliente('Maria', 18)

ct1 = ContaPoupanca(1111, 254136, 0)
ct2 = ContaCorrente(2222, 254137, 0)

cl1.inserir_conta(ct1)
cl2.inserir_conta(ct2)

b.inserir_cliente(cl1)
b.inserir_conta(ct1)

b.inserir_cliente(cl2)
b.inserir_conta(ct2)

if b.autenticar(cl1):
    cl1.ct.depositar(0)
    cl1.ct.sacar(20)
else:
    print('Cliente não autenticado.')

print('------------------')

if b.autenticar(cl2):
    cl2.ct.depositar(0)
    cl2.ct.sacar(20)
else:
    print('Cliente não autenticado.')
