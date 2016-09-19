from math import *
import random

##Jeu du 421
##
##variables utilisées : a,b,c,d,lancerRestant,r,x,nbrRelance,ChoixDés,s
##
##~Gautier plancq



x=1
lancerRestant=2

a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)


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


    print(" dé n°1 : ",a,"\n","dé n°2 : ",b,"\n","dé n°3 : ",c)

    if lancerRestant == 0:
        print("Vous n'avez plus de lancer !")
        x=0

    else:
        print("\nVoulez vous relancer ? (Il vous reste",lancerRestant,"lancer(s))")
        r=int(input("oui(1)/non(2) : "))

        while 1:
            if r == 1:
                break
            if r == 2:
                break
            else:
                r= 0
                r= int(input("oui(1)/non(2) : "))
                continue
            

        if r == 2:
            x=0

        else:
            lancerRestant=lancerRestant-1
            print("Combien de dés voulez-vous relancer ?")
            nbrRelance=int(input("1/2/3 ?: "))

            if nbrRelance == 1:
                choixDés=int(input("Choisissez quel dé voulez vous relancer.\n1/2/3 : "))
                if choixDés == 1:
                    a = random.randint(1,6)
                    
                if choixDés == 2:
                    b = random.randint(1,6)
                    
                if choixDés == 3:
                    c = random.randint(1,6)
                    

            if nbrRelance == 2:
                choixDés1=int(input("Choisissez quel dé voulez vous relancer.\n1/2/3 : "))
                choixDés2=int(input("Choisissez quel dé voulez vous relancer.\n1/2/3 : "))
                if choixDés1 == 1:
                    a = random.randint(1,6)   ## Cette partie  doit être recodé

                if choixDés1 == 2:            
                    b = random.randint(1,6)   ## 
                    
                if choixDés1 == 3:  
                    c = random.randint(1,6)   ## A.R
                    
                if choixDés2 == 1:     
                    a = random.randint(1,6)   ## A.R (besoin condit. éviter bugs)

                if choixDés2 == 2:            
                    b = random.randint(1,6)   ##
                    
                if choixDés2 == 3:
                    c = random.randint(1,6)   ## Cette partie  doit être recodé

            if nbrRelance == 3:
                a = random.randint(1,6)
                b = random.randint(1,6)
                c = random.randint(1,6)
            

s=a*100+b*10+c
print("\nVotre score est",s)
        
        
       ##Bug dans la relance de dés , fin du code à modif.
