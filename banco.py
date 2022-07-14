class Banco:
    def __init__(self):
        self.ags = [1111, 2222, 3333]
        self.cls = []
        self.cts = []

    def inserir_cliente(self, cl):
        self.cls.append(cl)

    def inserir_conta(self, ct):
        self.cts.append(ct)

    def autenticar(self, cl):
        if cl not in self.cls:
            return False

        if cl.ct not in self.cts:
            return False

        if cl.ct.ag not in self.ags:
            return False

        return True
