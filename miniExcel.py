import math
from tkinter import *
class miniExcel:
    def __init__(self, cols:int, rows:int) -> None:
        self.cols = cols
        self.rows = rows
        self.gui=Tk();
        self.gui.title("Mini Excel")
        #self.gui.resizable(False, False)
        self.gui.update()
        #self.gui.bind("<Configure>", lambda event: self.resize())
        self.GUI()
    def resize(self):
        altura = self.gui.winfo_width()
        anchura = self.gui.winfo_height()
        self.createTable()
    def GUI(self):
        self.createTable()
        self.gui.update()
        self.resize()
        self.gui.mainloop()
    def createTable(self):
        self.gui.update()
        rows = self.rows
        cols = self.cols
        #agrega un fila de con los nombres de las columnas A, B, C, etc        
        for j in range(1,cols+1):
            label = Label(self.gui, text=chr(ord('A')+j-1), width=10, fg='black', justify='center', font=('Arial',11))
            label.grid(row=0, column=j)

        # Agregar una columna con los nombres de las filas 1, 2, 3, etc
        for i in range(1, rows+1):
            label = Label(self.gui, text=str(i), width=5, fg='black', justify='center', font=('Arial',11))
            label.grid(row=i, column=0)

        # Dibujar una tabla de N*N celdas
        for i in range(1, rows+1):
            for j in range(1, cols+1): 
                self.e = Entry(self.gui, width=10, fg='black', justify='center', font=('Arial',11))
                self.e.grid(row=i, column=j)
                self.e.insert(END,"")
miniExcel(10,20)
