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

#brzina zmije
difficulty=4

#crtanje mape
def mapa():
    tMapa.pu(); tMapa.goto(-350,350); tMapa.pd(); tMapa.color('lightgray')
    tMapa.begin_fill()
    for q in range(4):
        tMapa.fd(700); tMapa.rt(90)
    tMapa.end_fill()
    tMapa.pu(); tMapa.goto(-250,250); tMapa.pd(); tMapa.color('black')
    tMapa.begin_fill()
    for q in range(4):
        tMapa.color('black'); tMapa.fd(500); tMapa.rt(90)
    tMapa.color('white'); tMapa.end_fill()
    

def roundto(x):
    y=round(x/50)
    return y*50

#funkcije za kretanje zmije
def up(a):
    if turt.heading()==270:
        return
    else:
        turt.seth(90)

def right(a):
    if turt.heading()==180:
        return
    else:
        turt.seth(0)

def down(a):
    if turt.heading()==90:
        return
    else:
        turt.seth(270)

def left(a):
    if turt.heading()==0:
        return
    else:
        turt.seth(180)

#restarta igricu i obnavlja početne vrijednosti
def restart(a):
    global putanja
    restartButton.config(text='RESTARTING...', state='disabled', relief='sunken')
    duljina.config(text='2/81')
    win.config(text=' ')
    turt.goto(-200,200); turt.seth(0)
    putanja=[[-200,200]]
    mapa(); hrana()
    sleep(2)
    restartButton.config(text='RESTART', state='active', relief='raised')
    move()


