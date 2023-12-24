from Nodo import Nodo

class Lista:
    def __init__(self) -> None:
        self.Head = None
        self.Tail = None
    def crearNodo(self, Data: int):
        aux = Nodo(Data)
        aux.setLink(self.Head)
        self.Head = aux

    def imprimirLista(self):
        aux = self.Head
        while aux != None:
            print(aux.getValor(), end=" -> ")
            aux = aux.getLink()
        print("None")

    def cantNodos(self):
        aux = self.Head
        cant = 0
        while aux != None:
            cant += 1
            aux = aux.getLink()
        return cant

    def getInPos(self, pos:int):
        if pos > self.cantNodos():
            print("[LISTA] Posicion inexistente")
            return
        aux = self.Head
        for _ in range(pos):
            aux = aux.getLink()
        return aux.getValor() 
    
    def setInPos(self, pos:int, Data:int):
        if pos > self.cantNodos():
            print("[LISTA] Posicion inexistente")
            return
        aux = self.Head
        for _ in range(1, pos):
            aux = aux.getLink()
        aux.setValor(Data)



