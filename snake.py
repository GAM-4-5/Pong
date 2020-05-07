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

#konfiguriranje postavki igre(težina igre)
def options(a):
    global go
    go=0
    def closeWin(a):   #zatvara prozor za postavke igre bez spremanja promjena
        global go
        go=1
        optionsButton.config(state='active', relief='raised')
        optionWin.destroy()
    def closeAccept(a):    #zatvara prozor za postavke igre i sprema promjene
        global difficulty; global go
        go=1
        optionsButton.config(state='active', relief='raised')
        if difficultyINT.get()!=0:
            difficulty=difficultyINT.get()
            optionWin.destroy()

    #prikazuje prozor postavki igre i definira dimenzije,boje itd.
    optionWin=Toplevel(window)
    optionWin.title('Options')
    optionWin.geometry('300x250+{}+{}'.format(window.winfo_x()+100, window.winfo_y()+100))
    optionWin.configure(bg='lightgray')
    optionsButton.config(state='disabled', relief='sunken')
    #gumb za spremanje promjena postavki
    closeAcceptButton=Button(optionWin, text='Apply and Close', font=(None,10,'bold'))
    closeAcceptButton.bind('<Button>', closeAccept)
    closeAcceptButton.place(x=130,y=200)
    #gumb za zatvaranje prozora postavki
    closeButton=Button(optionWin, text='Close', font=(None,10,'bold'))
    closeButton.bind('<Button>', closeWin)
    closeButton.place(x=80,y=200)
    difficultyINT=IntVar()   #težina igre
    #label u kojem su prikazane težine igre
    diffText=Label(optionWin, text='Difficulty', font=(None,17,'bold'), bg='lightgray')
    diffText.place(x=0,y=0)
    if difficulty==4:
        diffText.configure(text='Difficulty: Easy')
    elif difficulty==3:
        diffText.configure(text='Difficulty: Normal')
    elif difficulty==2:
        diffText.configure(text='Difficulty: Hard')
    elif difficulty==1:
        diffText.configure(text='Difficulty: Extreme')
    #buttoni za odabir težine igre   
    Radiobutton(optionWin, text='Easy', variable=difficultyINT, value=4, font=(None,12,'bold'), bg='lightgray').place(x=5,y=30)
    Radiobutton(optionWin, text='Normal', variable=difficultyINT, value=3, font=(None,12,'bold'), bg='lightgray').place(x=5,y=60)
    Radiobutton(optionWin, text='Hard', variable=difficultyINT, value=2, font=(None,12,'bold'), bg='lightgray').place(x=5,y=90)
    Radiobutton(optionWin, text='Extreme', variable=difficultyINT, value=1, font=(None,12,'bold'), bg='lightgray').place(x=5,y=120)

#prikazuje sliku hrane u random bojama
def hrana():
    tHrana.color(choice(['red','blue','brown','orange','purple']))
    tHrana.seth(randint(0,360))
    a=randint(-4,4); b=randint(-4,4)
    a=a*50; b=b*50
    if [a,b] in putanja:  #ako se hrana nalazi na istom mjestu kao i zmija,prikazuje se nova slika hrane na random poziciji
        hrana()
    else:
        tHrana.goto(a,b); tHrana.stamp()

#pomicanje zmije 
def move():
    go=1
    while go:
        turt.st(); turt.stamp()
        if turt.heading()==0:
            turt.goto(putanja[-1][0]+50,putanja[-1][1])
        elif turt.heading()==90:
            turt.goto(putanja[-1][0],putanja[-1][1]+50)
        elif turt.heading()==180:
            turt.goto(putanja[-1][0]-50,putanja[-1][1])
        elif turt.heading()==270:
            turt.goto(putanja[-1][0],putanja[-1][1]-50)            
        putanja.append([roundto(turt.xcor()),roundto(turt.ycor())])
        #provjerava da li se zmija nalazi na istim koordinatama kao i hrana
        if putanja[-1][0]==roundto(tHrana.xcor()) and putanja[-1][1]==roundto(tHrana.ycor()):
            duljina.config(text='{}/81'.format(len(putanja)+1))    #label sa rezultatom
            if len(putanja)<80:         #ako je duljina zmije manja od 80 prikazuje novu hranu
                hrana()
        else:
            tDel.goto(putanja[0][0],putanja[0][1]); tDel.stamp()
            putanja.pop(0)
        turt.stamp()
        #provjerava da li je zmija unutar mape
        if putanja[-1] in putanja[0:-1]:
            win.config(text='GAME OVER', fg='red')
            return
        if 250 in putanja[-1] or -250 in putanja[-1]:
            win.config(text='GAME OVER', fg='red')
            return
        #provjera duljine zmije/provjera za pobjedu
        if len(putanja)==80:
            win.config(text='YOU WON', fg='green')
            return
        sleep(difficulty*0.04)
        
window.bind('<Up>',up)
window.bind('<Right>',right)
window.bind('<Down>',down)
window.bind('<Left>',left)

win=Label(text=' ', font=(None,20,'bold'), width=10, bg='lightgray')
win.place(x=592,y=350)

#label koji prikazuje rezultat(duljinu)
duljina=Label(text='0/81', font=(None,25,'bold'), width=7)
duljina.place(x=570,y=50)

#button za restart
restartButton=Button(text='START', font=(None,15,'bold'), width=15)
restartButton.bind('<Button>', restart)
restartButton.place(x=585,y=450)
window.bind('<Return>', restart)

#options button sa slikom
optionsPNG=PhotoImage(file='options.png')
optionsButton=Button(image=optionsPNG)
optionsButton.bind('<Button>',options)
optionsButton.place(x=725,y=44)

#label u kojem su prikazane upute za igranje igre
tip=Label(text='play with the arrow keys start/restart with enter', font=(None,9,'bold'), wraplength=200, bg='lightgray')
tip.place(x=605,y=500)

#pokretanje igre
mapa()

window.mainloop()




