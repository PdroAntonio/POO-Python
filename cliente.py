class Pessoa:
    def __init__(self, n, i):
        self._n = n
        self._i = i

    @property
    def nome(self):
        return self._n

    @property
    def idade(self):
        return self._i


class Cliente(Pessoa):
    def __init__(self, n, i):
        super().__init__(n, i)
        self.ct = None

    def inserir_conta(self, ct):
        self.ct = ct
