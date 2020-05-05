#importanje potrebnih modula
from tkinter import * 
from turtle import *
from random import *
from time import *  

#definiranje tkinter prozora(određivanje dimenzija itd.)
window=Tk()
window.geometry('800x550')
window.title('Snake v7')
window.configure(bg='lightgray',bd=0)
window.resizable(False,False)
wincanvas=Canvas(window, width=550, height=550, bd=0)
wincanvas.place(x=0,y=0)

#definiranje zmije,hrane i polja
turt=RawTurtle(wincanvas)
tDel=RawTurtle(wincanvas)
tMapa=RawTurtle(wincanvas)
tHrana=RawTurtle(wincanvas)

#određivanje dimenzija boje i oblika za zmiju,hranu 
turt.speed(0); turt.shapesize(2.2,2.2); turt.shape('square'); turt.color('green'); turt.pu(); turt.ht()
tDel.speed(0); tDel.shapesize(2.2,2.2); tDel.shape('square'); tDel.color('white'); tDel.pu(); tDel.ht()
tHrana.speed(0); tHrana.shapesize(1.2,1.2); tHrana.shape('turtle'); tHrana.pu(); tHrana.ht()
tMapa.speed(0); tMapa.width(35); tMapa.ht() #određivanje dimenzija za mapu



