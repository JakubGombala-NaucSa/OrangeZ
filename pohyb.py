import tkinter as tk
from random import *

canvas = tk.Canvas(bg="white", width=500, height=500)
canvas.pack()

def lopticka(x,y,farba,Tag):
    canvas.create_oval(x+10,y+10,x-10,y-10,fill=farba,tag=Tag)
farby = ["red", "green","blue","pink","red", "green","blue","pink","blue","pink"]

def Start():
    canvas.delete("all")
    global x, y, medzera
    x = 20
    y = [20]*10
    medzera = 30
    for i in range(10):
        lopticka(x+medzera*i,y[i],farby[i], "lopticka"+str(i))
    pohyb()

def pohyb():
    global x, y, medzera
    for i in range(10):
        canvas.delete("lopticka"+str(i))
        y[i] += randint(1,10)
        lopticka(x+medzera*i,y[i],farby[i], "lopticka"+str(i))
        if y[i] >= 500-10:
            vyhodnotenie(i+1)
            return
    canvas.after(100, pohyb)

def vyhodnotenie(poradie):
    canvas.create_text(200,20,text="Vyhrala lopticka "+str(poradie),fill=farby[poradie-1])

button = tk.Button(text="Start", command=Start)
button.pack()
