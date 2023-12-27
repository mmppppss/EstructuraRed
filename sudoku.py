from Red import Red
from random import randint
import random
class sudoku:
    def __init__(self) -> None:
        self.red = Red(9)
    
    def iniciar(self):
        #crea un vector de 9 con digitos random;
        semilla = [1,2,3,4,5,6,7,8,9]
        random.shuffle(semilla)

sud = sudoku()
sud.iniciar()
