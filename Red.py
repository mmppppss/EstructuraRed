from Lista import Lista
class Red:
    def __init__(self, nListas:int) -> None:    
        self.Lista = [Lista() for _ in range(nListas)] # vector de n listas

    def insertar(self, nLista:int, valor:int):
        self.Lista[nLista].crearNodo(valor)

    def imprimirRed(self):
        for i in range(len(self.Lista)):
            self.Lista[i].imprimirLista()
     
    def getXY(self, nLista:int, pos:int):
        if nLista > len(self.Lista) or pos > self.Lista[nLista].cantNodos():
            print("[RED] Posicion inexistente")
            return
        return self.Lista[nLista].getInPos(pos)
     
    def getCol(self, nCol:int):
        aux=Lista()
        for i in range(len(self.Lista)):
            aux.crearNodo(self.Lista[i].getInPos(nCol))
        return aux

    def setInXY(self, x:int, y:int, valor:int):
        if(x-1 < len(self.Lista)):
            self.Lista[x-1].setInPos(y, valor)
        else:
            print("[RED] Posicion inexistente")

