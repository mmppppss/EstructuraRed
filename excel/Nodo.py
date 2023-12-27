class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.link = None
    def setLink(self, nodo):
        self.link = nodo
    def getLink(self):
        return self.link
    def setValor(self, valor:float):
        self.valor = valor
    def getValor(self):
        return self.valor
