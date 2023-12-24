import math
from time import sleep
from Red import Red
from tkinter import Tk, Canvas
red = Red(3)
gui = Tk();
gui.geometry("300x300");
canvas = Canvas(gui, width=300, height=300, bg="white")
class TTT: 

    def __init__(self):
        canvas.delete("all")
        self.use =[(-1,-1)] 
        self.crearTablero()
        self.Turno = False
        gui.title("Tic Tac Toe")
        self.graph()
    #ad onclick function for the canva
        canvas.bind("<Button-1>", lambda event: self.drawX0(event.x, event.y,self.Turno)) 
        canvas.pack()
        gui.mainloop()

    def graph(self):
    #draw a 3*3 grid 
        canvas.create_line(0, 100, 300, 100, width=10, fill="black")
        canvas.create_line(0, 200, 300, 200, width=10, fill="black")
        canvas.create_line(100, 0, 100, 300, width=10, fill="black")
        canvas.create_line(200, 0, 200, 300, width=10, fill="black")

    def drawX0(self,x,y, turno):
        posX=math.floor(x/100)
        posY=math.floor(y/100)
        a=(posX,posY)
        if a in self.use:
            return
        self.use.append(a)
        if(turno):
            canvas.create_oval(20+posX*100,20+posY*100,80+posX*100,80+posY*100, fill="black")
            canvas.create_oval(30+posX*100,30+posY*100,70+posX*100,70+posY*100, fill="white")
            self.Turno = False
            red.setInXY(posY, posX, 0) #O
        else:
            canvas.create_line(20+posX*100, 20+posY*100, 80+posX*100, 80+posY*100, width=10, fill="black")
            canvas.create_line(80+posX*100, 20+posY*100, 20+posX*100, 80+posY*100, width=10, fill="black")
            self.Turno = True
            red.setInXY(posY, posX, 1) #X
        canvas.pack()
        self.win()
    def crearTablero(self):
        for i in range(3):
            for j in range(3):
                red.insertar(i, -1)           
    def win(self):
        for i in range(3):
            a=red.getCol(i)
            if(a.getInPos(0)==a.getInPos(1)==a.getInPos(2)):
                if a.getInPos(0)==0: self.showWin("Gana O")
                if a.getInPos(0)==1: self.showWin("Gana X")
            a=red.getFil(i)
            if(a.getInPos(0)==a.getInPos(1)==a.getInPos(2)):
                if a.getInPos(0)==0: self.showWin("Gana O")
                if a.getInPos(0)==1: self.showWin("Gana X")
        x=red.getFil(0).getInPos(0)
        y=red.getFil(1).getInPos(1)
        z=red.getFil(2).getInPos(2)
        if(x==y==z):
            if x==0: self.showWin("Gana O")
            if x==1: self.showWin("Gana X")
        x=red.getFil(0).getInPos(2)
        y=red.getFil(1).getInPos(1)
        z=red.getFil(2).getInPos(0)
        if(x==y==z):
            if x==0: self.showWin("Gana O")
            if x==1: self.showWin("Gana X")
        count=0
        for i in range(9):
            a=red.getXY(i%3, i//3)
            if(a==0 or a==1):
                count+=1
        if count==9: self.showWin("Empate")
    def showWin(self, win:str):
        canvas.bind("<Button-1>", lambda event: TTT()) 
        canvas.create_text(150, 130, text=win, fill="red", font="Arial 50 bold")
        canvas.create_text(150, 170, text="Click para reiniciar", fill="red", font="Arial 24 bold")
##main
TTT()
