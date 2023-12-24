from random import randint
from Red import Red
from Nodo import Nodo
n=3
R=Red(n)
for i in range(n):
    for j in range(n):
        R.insertar(i, randint(0,9))
'''
R.insertar(0,1)
R.insertar(0,2)
R.insertar(0,3)
R.insertar(1,4)
R.insertar(1,5)
R.insertar(1,6)
R.insertar(2,7)
R.insertar(2,8)
R.insertar(2,9)
'''
R.imprimirRed()
print()
R.setInXY(3,33,10)
R.imprimirRed()
a=R.getCol(1)
print(type(a))
a.imprimirLista()
a.setInPos(1, 20)
a.imprimirLista()
aux=a
i=0

