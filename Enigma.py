# Commercial Enigma A 1924
#
# Ce programme permet de crypter un mot et le decrypter comme la machine Enigma
# utilisee durant la seconde guerre mondiale par les forces de l'axes.
#
# Valentin Coppin; Sebastien Santerre; Jean Ruellan

from tkinter import *
touche=0 #Correspond a la touche appuyee


#Code adressage des rotors
rotor1 = [12, 25, 16, 10, 19, 3, 5, 7, 16, 23, 6, 4, 10, 18, 16, 14, 1, 10, 3, 14, 5, 7, 13, 13, 21, 21]
rotor1x = [-25, -10, -7, -14, 10, -18, -23, -14, -3, -13, -13, -5, -12, -10, -7, -4, -6, -1, -16, -21, -21, -3, -10, -19, -16, -5]
r1 = 0
rotation1 = 0

rotor2=[10,19,3,5,7,16,23,6,4,10,18,16,14,1,10,3,14,5,7,13,13,21,21,12,25,16]
rotor2x=[-14,10,-18,-23,-14,-3,-13,-13,-5,-12,-10,-7,-4,-6,-1,-16,-21,-21,-3,-10,-19,-16,-5,-25,-10,-7]
r2=0
rotation2 = 0

rotor3=[6,4,10,18,16,14,1,10,3,14,5,7,13,13,21,21,12,25,16,10,19,3,5,7,16,23]
rotor3x=[-13,-5,-12,-10,-7,-4,-6,-1,-16,-21,-21,-3,-10,-19,-16,-5,-25,-10,-7,-14,10,-18,-23,-14,-3,-13]
r3=0
rotation3 = 0

reflector=[25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

NombreDeLettre=int(26)

# Permet la rotation des rotors
def rotation():
    global r1
    global r2
    global r3
    if r1==NombreDeLettre-1 :
        r1=0
        rotor1.append(rotor1[0])
        del(rotor1[0])
        rotor1x.append(rotor1x[0])
        del(rotor1x[0])

        if r2==NombreDeLettre-1:
            r2=0
            rotor2.append(rotor2[0])
            del(rotor2[0])

            rotor2x.append(rotor2x[0])
            del(rotor2x[0])

            if r3==NombreDeLettre-1:
                r3=0
                rotor3.append(rotor3[0])
                del(rotor3[0])

                rotor3x.append(rotor3x[0])
                del(rotor3x[0])

            else:
                r3=r3+1
                rotor3.append(rotor3[0])
                del(rotor3[0])

                rotor3x.append(rotor3x[0])
                del(rotor3x[0])

        else:
            r2=r2+1
            rotor2.append(rotor2[0])
            del(rotor2[0])
            rotor2x.append(rotor2x[0])
            del(rotor2x[0])
    else:
        r1 = r1+1
        rotor1.append(rotor1[0])
        del(rotor1[0])
        rotor1x.append(rotor1x[0])
        del(rotor1x[0])

#Permet de crypter la lettre rentrée
def crypting(x):
    x = (int(rotor1[x])+x)%NombreDeLettre
    x = (int(rotor2[x])+x)%NombreDeLettre
    x = (int(rotor3[x])+x)%NombreDeLettre
    x = int(reflector[x])%NombreDeLettre
    x = (x+rotor3x[x])%NombreDeLettre
    x = (x+rotor2x[x])%NombreDeLettre
    x = (x+rotor1x[x])%NombreDeLettre
    allumage(x)

#Permet de coordonner toutes les taches lors du cryptage et d'actualiser l'interface utilisateur
def action(event, x):
    Effacer()
    crypting(x)
    rotation()
    Canevas.itemconfig(Labelr1, text=r1)
    Canevas.itemconfig(Labelr2, text=r2)
    Canevas.itemconfig(Labelr3, text=r3)

#Boutons de réglage des rotors (6)
def Rotation1Plus():
    rotation()
    Canevas.itemconfig(Labelr1, text=r1)
    Canevas.itemconfig(Labelr2, text=r2)
    Canevas.itemconfig(Labelr3, text=r3)

def Rotation2Plus():
    for n in range (0,26):
        rotation()
    Canevas.itemconfig(Labelr1, text=r1)
    Canevas.itemconfig(Labelr2, text=r2)
    Canevas.itemconfig(Labelr3, text=r3)

def Rotation3Plus():
    for n in range (0,26*26):
        rotation()
    Canevas.itemconfig(Labelr1, text=r1)
    Canevas.itemconfig(Labelr2, text=r2)
    Canevas.itemconfig(Labelr3, text=r3)

def Rotation1Moins():
    for x in range (0,26*26*26-1):
        rotation()
    Canevas.itemconfig(Labelr1, text=r1)
    Canevas.itemconfig(Labelr2, text=r2)
    Canevas.itemconfig(Labelr3, text=r3)

def Rotation2Moins():
    for n in range (0,26*26*26-26):
        rotation()
    Canevas.itemconfig(Labelr1, text=r1)
    Canevas.itemconfig(Labelr2, text=r2)
    Canevas.itemconfig(Labelr3, text=r3)

def Rotation3Moins():
    for n in range (0,26*26*26-26*26):
        rotation()
    Canevas.itemconfig(Labelr1, text=r1)
    Canevas.itemconfig(Labelr2, text=r2)
    Canevas.itemconfig(Labelr3, text=r3)

#Permer d'initialiser toutes les objets qui permette d'afficher les lettres
def initAllumage():
    for x in range (0,26):
        allumage(x)
    Effacer()


#Permet de savoir savoir où l'utilisateur a cliqué
def Clic(event):
    """ Gestion de l'ÃƒÂ©vÃƒÂ¨nement Clic gauche sur la zone graphique """
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    #test des zones de clic
    if 90<X<125 and 383<Y<414:
        #print("Q")
        action(event, 16)

    if 146<X<179 and 383<Y<414:
        #print("W")
        action(event, 22)

    if 203<X<235 and 383<Y<414:
        #print("E")
        action(event, 4)

    if 260<X<291 and 383<Y<414:
        #print("R")
        action(event, 17)

    if 316<X<347 and 383<Y<414:
        #print("T")
        action(event, 19)

    if 371<X<405 and 383<Y<414:
        #print("Z")
        action(event, 25)

    if 426<X<460 and 383<Y<414:
        #print("U")
        action(event, 20)

    if 483<X<514 and 383<Y<414:     #A Verifier dans fiche alphaber.numbers
        #print("I")
        action(event, 8)

    if 538<X<570 and 383<Y<414:
        #print("O")
        action(event, 14)

    if 109<X<143 and 435<Y<466:
        #print("A")
        action(event, 0)

    if 166<X<198 and 435<Y<466:
        #print("S")
        action(event, 18)

    if 221<X<255 and 435<Y<466:
        #print("D")
        action(event, 3)

    if 277<X<312 and 435<Y<466:
        #print("F")
        action(event, 5)

    if 336<X<368 and 435<Y<466:
        #print("G")
        action(event, 6)

    if 388<X<425 and 435<Y<466:
        #print("H")
        action(event, 7)

    if 447<X<480 and 435<Y<466:
        #print("J")
        action(event, 9)

    if 503<X<534 and 435<Y<466:
        #print("K")
        action(event, 10)

    if 68<X<101 and 490<Y<521 :
        #print("P")
        action(event, 15)

    if 124<X<160 and 490<Y<521 :
        #print("Y")
        action(event, 24)

    if 183<X<216 and 490<Y<521 :
        #print("X")
        action(event, 23)

    if 240<X<273 and 490<Y<521 :
        #print("C")
        action(event, 2)

    if 298<X<328 and 490<Y<521 :
        #print("V")
        action(event, 21)

    if 355<X<386 and 490<Y<521 :
        #print("B")
        action(event, 1)

    if 410<X<444 and 490<Y<521 :
        #print("N")
        action(event, 13)

    if 467<X<500 and 490<Y<521 :
        #print("M")
        action(event, 12)

    if 522<X<556 and 490<Y<521 :
        #print("L")
        action(event, 11)

#Permet d'effacer la dernière lettre crypté
def Effacer():
    Canevas.delete(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z)

#Permet d'allumer la bonne lettre une fois crypté
def allumage(x):
    global A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
    if x==0:
       A = Canevas.create_oval(115, 279, 148, 309, outline="#E8CC06", width = 3)

    if x==1:
       B = Canevas.create_oval(350, 322, 382, 353, outline="#E8CC06", width = 3)

    if x==2:
       C = Canevas.create_oval(239, 322, 274, 353, outline="#E8CC06", width = 3)

    if x==3:
       D = Canevas.create_oval(221, 279, 255, 309, outline="#E8CC06", width = 3)

    if x==4:
       E = Canevas.create_oval(204, 265, 241, 238, outline="#E8CC06", width = 3)

    if x==5:
       F = Canevas.create_oval(274, 279, 309, 309, outline="#E8CC06", width = 3)

    if x==6:
       G = Canevas.create_oval(328, 279, 363, 309, outline="#E8CC06", width = 3)

    if x==7:
       H = Canevas.create_oval(382, 279, 416, 309, outline="#E8CC06", width = 3)

    if x==8:
       I = Canevas.create_oval(467, 265, 500, 238, outline="#E8CC06", width = 3)

    if x==9:
       J = Canevas.create_oval(435, 279, 469, 309, outline="#E8CC06", width = 3)

    if x==10:
       K = Canevas.create_oval(488, 279, 522, 309, outline="#E8CC06", width = 3)

    if x==11:
       L = Canevas.create_oval(512, 322, 545, 353, outline="#E8CC06", width = 3)

    if x==12:
       M = Canevas.create_oval(458, 322, 488, 353, outline="#E8CC06", width = 3)

    if x==13:
       N = Canevas.create_oval(403, 323, 437, 353, outline="#E8CC06", width = 3)

    if x==14:
       O = Canevas.create_oval(520, 265, 552, 238, outline="#E8CC06", width = 3)

    if x==15:
       P = Canevas.create_oval(77, 322, 108, 353, outline="#E8CC06", width = 3)

    if x==16:
       Q = Canevas.create_oval(101, 265, 132, 238, outline="#E8CC06", width = 3)

    if x==17:
       R = Canevas.create_oval(257, 265, 292, 238, outline="#E8CC06", width = 3)

    if x==18:
       S = Canevas.create_oval(167, 279, 202, 309, outline="#E8CC06", width = 3)

    if x==19:
       T = Canevas.create_oval(310, 265, 344, 238, outline="#E8CC06", width = 3)

    if x==20:
       U = Canevas.create_oval(416, 265, 448, 238, outline="#E8CC06", width = 3)

    if x==21:
       V = Canevas.create_oval(297, 322, 326, 353, outline="#E8CC06", width = 3)

    if x==22:
       W = Canevas.create_oval(153, 265, 186, 238, outline="#E8CC06", width = 3)

    if x==23:
       X = Canevas.create_oval(186, 322, 219, 353, outline="#E8CC06", width = 3)

    if x==24:
       Y = Canevas.create_oval(132, 322, 165, 353, outline="#E8CC06", width = 3)

    if x==25:
       Z = Canevas.create_oval(362, 265, 395, 238, outline="#E8CC06", width = 3)



# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Enigma - COPPIN RUELLAN SANTERRE')

# Création d'un widget Canvas (zone graphique)
Largeur = 638
Hauteur = 634
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
Canevas.grid(padx =5, pady =5)

# Création d'un widget Button (bouton Quitter)
BouttonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BouttonQuitter.grid(row = 3, column = 1, padx = 0, pady = 0)

#Création des boutons permettant de régler les rotors
ButtonPlusR1 = Button(Mafenetre, text = '+',command = Rotation1Plus )
ButtonPlusR1.place(x=330, y=55)

ButtonMoinsR1 = Button(Mafenetre, text = '-', command = Rotation1Moins )
ButtonMoinsR1.place(x=330, y=205)

ButtonPlusR2 = Button(Mafenetre, text = '+', command = Rotation2Plus  )
ButtonPlusR2.place(x=270, y=55)

ButtonMoinsR2 = Button(Mafenetre, text = '-', command = Rotation2Moins )
ButtonMoinsR2.place(x=270, y=205)

ButtonPlusR3 = Button(Mafenetre, text = '+', command = Rotation3Plus )
ButtonPlusR3.place(x=210, y=55)

ButtonMoinsR3 = Button(Mafenetre, text = '-', command = Rotation3Moins )
ButtonMoinsR3.place(x=210, y=205)

#Création du label indiquant la position du rotor
Labelr1 = Canevas.create_text(317, 150, text=r1)
Labelr2 = Canevas.create_text(260, 150, text=r2)
Labelr3 = Canevas.create_text(204, 150, text=r3)

#Insertion de l'image dans le Canvas:
fichier = PhotoImage(file="enigmaGIF.gif")
Canvas = Canevas.create_image(319,317,image = fichier)

#Initialisation des objets
initAllumage()

#Association du bouton à la fonction clic
Canevas.bind('<Button 1>',Clic)

#Permet d'utiliser les touches du clavier (physique)  pour utiliser Enigma
Mafenetre.focus_set()
Mafenetre.bind('<a>',lambda event : action(event, 0))
Mafenetre.bind('<b>',lambda event : action(event, 1))
Mafenetre.bind('<c>',lambda event : action(event, 2))
Mafenetre.bind('<d>',lambda event : action(event, 3))
Mafenetre.bind('<e>',lambda event : action(event, 4))
Mafenetre.bind('<f>',lambda event : action(event, 5))
Mafenetre.bind('<g>',lambda event : action(event, 6))
Mafenetre.bind('<h>',lambda event : action(event, 7))
Mafenetre.bind('<i>',lambda event : action(event, 8))
Mafenetre.bind('<j>',lambda event : action(event, 9))
Mafenetre.bind('<k>',lambda event : action(event, 10))
Mafenetre.bind('<l>',lambda event : action(event, 11))
Mafenetre.bind('<m>',lambda event : action(event, 12))
Mafenetre.bind('<n>',lambda event : action(event, 13))
Mafenetre.bind('<o>',lambda event : action(event, 14))
Mafenetre.bind('<p>',lambda event : action(event, 15))
Mafenetre.bind('<q>',lambda event : action(event, 16))
Mafenetre.bind('<r>',lambda event : action(event, 17))
Mafenetre.bind('<s>',lambda event : action(event, 18))
Mafenetre.bind('<t>',lambda event : action(event, 19))
Mafenetre.bind('<u>',lambda event : action(event, 20))
Mafenetre.bind('<v>',lambda event : action(event, 21))
Mafenetre.bind('<w>',lambda event : action(event, 22))
Mafenetre.bind('<x>',lambda event : action(event, 23))
Mafenetre.bind('<y>',lambda event : action(event, 24))
Mafenetre.bind('<z>',lambda event : action(event, 25))

Mafenetre.mainloop()