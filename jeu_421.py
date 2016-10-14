from math import *
import random

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

##Tirage trois dés
a = tirerNbrAlea()
b = tirerNbrAlea()
c = tirerNbrAlea()

##Mise en ordre des dés
while x==1:
    print("\n   ",a,b,c,"\n")

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

##Affichage
    print(" dé n°1 : ",a,"\n","dé n°2 : ",b,"\n","dé n°3 : ",c)

##Relance?
    if lancerRestant == 0:
        print("Vous n'avez plus de lancer !\n")
        x=0

    else:
        print("\nVoulez vous relancer ? (Il vous reste",lancerRestant,"lancer(s))")
        r=int(input("oui(1)/non(2) : "))

        while 1:
            if r == 1 or r == 2:
                break
            else:
                r= 0
                r= int(input("oui(1)/non(2) : "))
                continue
            

        if r == 2:
            x=0
##Relance des dés
        else:
            lancerRestant=lancerRestant-1
            print("Combien de dés voulez-vous relancer ?")
            control=1

            while control ==1:
                nbrRelance=int(input("1/2/3 ?: "))

                if nbrRelance == 1:
                    choixDés=int(input("Choisissez quel dé voulez vous relancer.\n1/2/3 : "))
                    testChoixDés(choixDés)
                        

                if nbrRelance == 2:
                    choixDés1=0
                    choixDés2=0

                    while 1:
                        choixDés1=int(input("Choisissez quel dé voulez vous relancer.\n1/2/3 : "))
            
                        if choixDés1 == 1 or choixDés1 == 2 or choixDés1 == 3:
                            break

                    while choixDés2 < 1 or choixDés2 >3 or choixDés2 == choixDés1:
        
                        choixDés2=int(input("Choisissez quel dé voulez vous relancer.\n1/2/3 : "))
                        
                    testChoixDés(choixDés1)
                        
                    testChoixDés(choixDés2)

                if nbrRelance == 3:
                    a = tirerNbrAlea()
                    b = tirerNbrAlea()
                    c = tirerNbrAlea()
                    control=0



##Print
print(" dé n°1 : ",a,"\n","dé n°2 : ",b,"\n","dé n°3 : ",c,"\n")

##Score:

if a == 4 and b == 2 and c == 1:
    score=10
elif a == 2 and b == 2 and c == 1:
    score=4
elif a == 1 and b == 1 and c == 1:
    score=7
elif a == 1 and b == 1 and c != 1:
    score=c
elif a == b+1 and b == c+1:
    score=2
elif a == b and b == c:
    score=a
else:
    score=1

##Fin Score


##Affichage score
s=a*100+b*10+c
print("Vous avez obtenu un score de ",score," points","avec ",s)

#Ecriture Fichier
save = open("score.txt","a+")
save.write(str(score)+"\n")
save.close()


        
        
       
