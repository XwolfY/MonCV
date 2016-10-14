from tkinter import*
from math import *
import random
import time

##Def fonctions

def tirerNbrAlea():
    x = random.randint(1,6)
    return x

def testChoixDés(choix):
    global a,b,c,control
    if choix == 1:
        a = tirerNbrAlea()
        control=0
                        
    if choix == 2:
        b = tirerNbrAlea()
        control=0
                        
    if choix == 3:
        c = tirerNbrAlea()
        control=0
        
##Jeu du 421
##
##variables utilisées : a,b,c,d,lancerRestant,r,x,nbrRelance,ChoixDés,s,control,score
##
##~Gautier plancq et Gaëtan Billaut


##Initialisation variables de contrôles
x=1
lancerRestant=2
j=0
if j==0:
    i=0
    j=1

##Tirage trois dés
a = tirerNbrAlea()
b = tirerNbrAlea()
c = tirerNbrAlea()
d=0
##Mise en ordre des dés
if a >= b:
    if a >= c:
        if b < c:
            d=c
            c=b
            b=d
    else:
        d=a
        a=c
        c=b
        b=d
else:
    if b < c:
        d=a
        a=c
        c=d
    else:
        if a < c:
            d=a
            a=b
            b=c
            c=d
        else:
            d=a
            a=b
            b=d 


fe= Tk()
fe.title('421.PreAlpha')
fe.geometry('400x300+425+350')
fe['bg']="white"
fe.resizable(0,0)

##De1 = Label(fe,text="Dés 1: ",fg="blue").grid(row=1,column=0)
##De1Var = Label(fe,text=a,fg="red").grid(row=1,column=1,padx=2)
##De2 = Label(fe,text="Dés 2: ",fg="blue").grid(row=1,column=3)
##De2var= Label(fe,text=b,fg="red").grid(row=1,column=4,padx=4)
##De3 = Label(fe,text="Dés 3: ",fg="blue").grid(row=1,column=5)
##De3var= Label(fe,text=c,fg="red").grid(row=1,column=6)
if i<=2:
    Frame1 = Frame(fe)
    Frame1.grid(row=1,column=0,padx=110,pady=55)
    Label(Frame1,text="421",fg="Black",bg='white',font=('Impact',96)).grid(row=1,column=0)
    i=i+1
if i==2:
    time.sleep(3)
    Frame1.destroy()
fe.mainloop()
    
##Button(Frame1,text="Effacer",fg='navy',command=Frame1.destroy).grid(row=1,column=2)
