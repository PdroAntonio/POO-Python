from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, ag, ct, sl):
        self.ag = ag
        self.ct = ct
        self.sl = sl

    def depositar(self, v):
        self.sl += v
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.ag} '
              f'Conta: {self.ct} '
              f'Saldo: {self.sl}')

    @abstractmethod
    def sacar(self, v): pass


class ContaPoupanca(Conta):
    def sacar(self, v):
        if self.sl < v:
            print('Saldo insuficiente')
            return

        self.sl -= v
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, ag, ct, sl, limite=100):
        super().__init__(ag, ct, sl)
        self.limite = limite

    def sacar(self, v):
        if (self.sl + self.limite) < v:
            print('Saldo insuficiente')
            return

        self.sl -= v
        self.detalhes()
