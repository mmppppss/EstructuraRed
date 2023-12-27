import math
from re import I
from Red import Red
from tkinter import *
class miniExcel:
    def __init__(self, cols:int, rows:int) -> None:
        #crea una matriz de 10x20
        self.celdas= [[Entry() for i in range(cols)] for j in range(rows)]
        self.cols = cols
        self.rows = rows
        self.gui=Tk();
        self.gui.title("Mini Excel")
        self.gui.update()
        self.red=Red(rows)
        self.createRed();
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
                #agregar eventos terminar de escribir o focus out
                self.e.bind("<FocusOut>", lambda event, row=i-1, col=j-1: self.loadData(row, col))
                self.celdas[i-1][j-1] = self.e
                self.e.insert(END,"")
    def createRed(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.red.insertar(i,0)
        self.red.imprimirRed() 
    def loadData(self, row:int, col:int):
            try:
                data=int(self.celdas[row][col].get())
                self.red.setInXY(row,col,data)
            except:
                func=self.celdas[row][col].get()
                self.funcion(func, row, col)
            #self.red.imprimirRed()
    def funcion(self, func:str, rowTable:int, colTable:int):
        args=func.split("(")[1].split(")")[0].split(",")
        nums=[]
        res=0
        #comprueba si el argumento es solo una letra
        for i in range(len(args)):
            if len(args[i])==1 and args[i].isalpha():
                col=list(args[i])[0] #A,B,C etc
                col=ord(col)-ord('A')-32
                list=self.red.getCol(col)
                while list.cantNodos() > 0:
                    nums.append(list.getInPos(0))
                    list.imprimirLista()
                    list=self.red.getCol(col)
                print("es solo una letra")
                break
            col=list(args[i])[0] #A,B,C etc
            col=ord(col)-ord('A')-32
            row=int(list(args[i])[1]) #1,2,3 etc
            nums.append(self.red.getXY(row-1,col))
        if func.startswith("sum"):
            res=sum(nums)
        elif func.startswith("max"):
            res=max(nums)
        elif func.startswith("min"):
            res=min(nums)
        elif func.startswith("abs"):
            res=abs(sum(nums))
        self.red.setInXY(rowTable,colTable,res)
        self.mostrarRedEnExcel()

    def mostrarRedEnExcel(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.celdas[i][j].delete(0,END)
                content = str(self.red.getXY(i,j)) if "0" not in str(self.red.getXY(i,j)) else ""
                self.celdas[i][j].insert(END,content)
miniExcel(5,5)
