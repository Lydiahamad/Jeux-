#La structure du code montre une implémentation du jeu Quadthello, intégrant la logique de jeu, la gestion des coups, les interactions joueur-ordinateur, et l'interface graphique avec Tkinter pour une expérience utilisateur visuelle.
#tkinter est utilisé pour créer l'interface graphique.
#random est utilisé pour générer des nombres aléatoires, en particulier pour la logique de jeu impliquant l'ordinateur.
import tkinter as tk
import random

# Crée une grille de hauteur h et de largeur l remplie de zéros
    # retourne la grille

def creer_grille(h,l):
    B=[]
    for i in range (h):
        B.append([])
        for j in range (l):
            B[i].append(0)
    return B

# Définition des classes

class Grille: # représente la grille de jeu avec une hauteur et une largeur définies
    def __init__(self, hauteur,largeur):
        self.hauteur=hauteur
        self.largeur=largeur
        self.tableau=creer_grille(hauteur, largeur)
    def get(self,x,y):#récupère la valeur à la position (x, y) de la grille
        return self.tableau[y][x]
    def set(self, x, y, val):# Place une valeur à la position (x, y) de la grille
        self.tableau[y][x]=val
    def afficher(self):#Affiche la grille dans la console.
        for i in range (len(self.tableau)):
            for j in range(len(self.tableau[i])):
                v=self.get(j,i)
                print(v,' ',end='')
            print('')
        print('')


class PlateauQuadthello: # représente le plateau de jeu avec ses paramètres et fonctionnalités spécifiques
    def __init__(self):  #initialisation des paramètres
        self.grille=Grille(8,10)
        self.joueur=1
        self.gains_jaunes1=0
        self.gains_jaunes2=0
        self.pions_joueur_1=[(4,4),(5,3)]
        self.pions_joueur_2=[(4,3),(5,4)]
        self.pions_yellow=[]
        self.mode_jeu='Ordinateur'
        self.placer_pions()
    def placer_pions(self):# Place les pions initiaux 
        self.grille.set(4,3,2)
        self.grille.set(5,4,2)
        self.grille.set(4,4,1)
        self.grille.set(5,3,1)
    def lister_coups_possibles(self,joueur):#retourne la liste des coups possibles d'un joueur.
        coups_possibles=[]
        for pions in zone_dessin.plateau.pions_yellow:
            voisins_indirects=[(pions[0]-1,pions[1]-1),(pions[0]-1,pions[1]+1),   (pions[0]+1,pions[1]-1),(pions[0]+1,pions[1]+1)]
            for x, y in voisins_indirects:
                if Coup(x,y,zone_dessin.plateau,joueur).est_valide()==True and (x,y) not in coups_possibles:
                    coups_possibles.append((x,y))
        if joueur==1:
            for pions in zone_dessin.plateau.pions_joueur_1:
                voisins_directs=[(pions[0],pions[1]-1),(pions[0]-1,pions[1]),   (pions[0],pions[1]+1),(pions[0]+1,pions[1])]
                for x, y in voisins_directs:
                    if Coup(x,y,zone_dessin.plateau,joueur).est_valide()==True and (x,y) not in coups_possibles:
                        coups_possibles.append((x,y))
        else:
            for pions in zone_dessin.plateau.pions_joueur_2:
                voisins_directs=[(pions[0],pions[1]-1),(pions[0]-1,pions[1]),   (pions[0],pions[1]+1),(pions[0]+1,pions[1])]
                for x, y in voisins_directs:
                    if Coup(x,y,zone_dessin.plateau,joueur).est_valide()==True and (x,y) not in coups_possibles:
                        coups_possibles.append((x,y))
        return coups_possibles



class Coup: #représente un coup sur le plateau
    def __init__(self,xp,yp,plateau,joueur): #Initialise un coup pour un joueur donné
        self.xp=xp
        self.yp=yp
        self.plateau=plateau
        self.joueur=joueur
    def est_dans_la_grille(self):
        largeur=self.plateau.grille.largeur
        hauteur=self.plateau.grille.hauteur
        return 0<=self.xp<largeur and 0<=self.yp<hauteur
    def case_est_libre(self):
        grille=self.plateau.grille
        return grille.get(self.xp,self.yp)==0
    def peut_placer_pion(self):
        grille=self.plateau.grille
        largeur=self.plateau.grille.largeur
        hauteur=self.plateau.grille.hauteur
        voisins_directs=[(self.xp,self.yp-1),(self.xp-1,self.yp),   (self.xp,self.yp+1),(self.xp+1,self.yp)]
        for x, y in voisins_directs :
            if 0<=x<largeur and 0<=y<hauteur and grille.get(x, y)==self.joueur:
                return True
        voisins_indirects=[(self.xp-1,self.yp-1),(self.xp-1,self.yp+1),(self.xp+1,self.yp-1),(self.xp+1,self.yp+1)]
        for x, y in voisins_indirects :
            if 0<=x<largeur and 0<=y<hauteur and grille.get(x, y)==3:
                return True
        return False
    def est_valide(self):
        return (self.est_dans_la_grille()==True and self.case_est_libre()==True and self.peut_placer_pion()==True)
    def lister_pions_a_jaunir(self):
        pions_a_jaunir=[]
        pions=[]
        nombre_voisins_joueur=0
        tous_les_voisins=[(self.xp,self.yp-1),(self.xp-1,self.yp),(self.xp,self.yp+1),(self.xp+1,self.yp),(self.xp-1,self.yp-1),(self.xp-1,self.yp+1),(self.xp+1,self.yp-1),(self.xp+1,self.yp+1)]
        if self.joueur==2:
            for x in tous_les_voisins:
                if Coup(x[0],x[1],plateau,plateau.joueur).est_dans_la_grille()==True:
                    if plateau.grille.get(x[0],x[1])==2:
                        pions.append((x[0],x[1]))
            for coord in pions:
                tous_les_voisins_coord=[(coord[0],coord[1]-1),(coord[0]-1,coord[1]),(coord[0],coord[1]+1),(coord[0]+1,coord[1]),(coord[0]-1,coord[1]-1),(coord[0]-1,coord[1]+1),(coord[0]+1,coord[1]-1),(coord[0]+1,coord[1]+1)]
                nombre_voisins_joueur=0
                for x in tous_les_voisins_coord:
                    if Coup(x[0],x[1],plateau,plateau.joueur).est_dans_la_grille()==True:
                        if plateau.grille.get(x[0],x[1])==1:
                            nombre_voisins_joueur+=1
                if nombre_voisins_joueur==4:
                    pions_a_jaunir.append((coord[0],coord[1]))
                    zone_dessin.liste_coup_jouer.pop()
                    zone_dessin.liste_coup_jouer.append((zone_dessin.xp,zone_dessin.yp,len(pions_a_jaunir)))
        else:
            for x in tous_les_voisins:
                if Coup(x[0],x[1],plateau,plateau.joueur).est_dans_la_grille()==True:
                    if plateau.grille.get(x[0],x[1])==1:
                        pions.append((x[0],x[1]))
            for coord in pions:
                tous_les_voisins_coord=[(coord[0],coord[1]-1),(coord[0]-1,coord[1]),(coord[0],coord[1]+1),(coord[0]+1,coord[1]),(coord[0]-1,coord[1]-1),(coord[0]-1,coord[1]+1),(coord[0]+1,coord[1]-1),(coord[0]+1,coord[1]+1)]
                nombre_voisins_joueur=0
                for x in tous_les_voisins_coord:
                    if Coup(x[0],x[1],plateau,plateau.joueur).est_dans_la_grille()==True:
                        if plateau.grille.get(x[0],x[1])==2:
                            nombre_voisins_joueur+=1
                if nombre_voisins_joueur==4:
                    pions_a_jaunir.append((coord[0],coord[1]))
                    zone_dessin.liste_coup_jouer.pop()
                    zone_dessin.liste_coup_jouer.append((zone_dessin.xp,zone_dessin.yp,len(pions_a_jaunir)))
        return pions_a_jaunir
    def jaunir_pions_de_liste(self, liste):
        for x in liste:
            plateau.grille.set(x[0],x[1],3)
            zone_dessin.plateau.pions_yellow.append((x[0],x[1]))
            if plateau.joueur==2:
                zone_dessin.plateau.gains_jaunes1+=1
            else:
                zone_dessin.plateau.gains_jaunes2+=1

class CoupJoue: #représente un coup joué.
    def __init__(self, xp, yp, pions_jaunis):
        self.xp = xp
        self.yp = yp
        self.pions_jaunis = pions_jaunis
    #La fonction "Défaire" enlève le dernier pion joué, annulant ainsi le mouvement précédent. En mode contre l'ordinateur, elle supprime à la fois le dernier pion de l'ordinateur et celui du joueur, ramenant le jeu à son état antérieur. En mode 2 joueurs, elle ne supprime que le dernier pion du joueur actuel, préservant les mouvements de l'autre joueur.
    def defaire(self, plateau):
        bouton_defaire["state"]=tk.DISABLED
        plateau.grille.set(self.xp,self.yp,0)
        if self.pions_jaunis!=[] and zone_dessin.liste_coup_jouer[-1][2]!=0:
            for pions_jaunis_au_dernier_coup in range (zone_dessin.liste_coup_jouer[-1][2]):
                plateau.grille.set(self.pions_jaunis[-1][0],self.pions_jaunis[-1][1],plateau.joueur)
                self.pions_jaunis.pop()
                if plateau.joueur==2:
                    zone_dessin.plateau.gains_jaunes1+=-1
                else:
                    zone_dessin.plateau.gains_jaunes2+=-1
        if zone_dessin.liste_coup_jouer!=[]:
            zone_dessin.liste_coup_jouer.pop()
        if zone_dessin.liste_coup_jouer!=[]:
            zone_dessin.xp=zone_dessin.liste_coup_jouer[-1][0]
            zone_dessin.yp=zone_dessin.liste_coup_jouer[-1][1]
        if plateau.joueur==2:
            zone_dessin.plateau.pions_joueur_1.pop()
            plateau.joueur=1
        else:
            zone_dessin.plateau.pions_joueur_2.pop()
            plateau.joueur=2
            if plateau.mode_jeu=='Ordinateur':
                plateau.grille.set(zone_dessin.xp,zone_dessin.yp,0)
                zone_dessin.plateau.pions_joueur_1.pop()
                if self.pions_jaunis!=[] and zone_dessin.liste_coup_jouer[-1][2]!=0:
                    for pions_jaunis_au_dernier_coup in range (zone_dessin.liste_coup_jouer[-1][2]):
                        plateau.grille.set(self.pions_jaunis[-1][0],self.pions_jaunis[-1][1],plateau.joueur)
                        self.pions_jaunis.pop()
                        zone_dessin.plateau.gains_jaunes1+=-1
                if zone_dessin.liste_coup_jouer!=[]:
                    zone_dessin.liste_coup_jouer.pop()
                if zone_dessin.liste_coup_jouer!=[]:
                    zone_dessin.xp=zone_dessin.liste_coup_jouer[-1][0]
                    zone_dessin.yp=zone_dessin.liste_coup_jouer[-1][1]
                plateau.joueur=1
        if plateau.mode_jeu=='Ordinateur':
            tout_dessiner(zone_dessin)
        else:
            tout_dessiner2(zone_dessin)


# initialisation

r=50    #r est le coté de chacune des cases du plateau, toutes les distances seront calculer en fonction de cette valeur
plateau = PlateauQuadthello()

# Fonctions tout dessiner


def dessiner_coups_possibles(zone_dessin,liste):#coups possibles sur le plateau
    for x,y in liste:
        zone_dessin.create_line((x+2.3)*r,(y+1.3)*r,(x+2.7)*r,(y+1.7)*r,fill="black")
        zone_dessin.create_line((x+2.7)*r,(y+1.3)*r,(x+2.3)*r,(y+1.7)*r,fill="black")


def fin_de_partie(zone_dessin): #Affiche le gagnant à la fin du jeu dans une fenêtre graphique.
    zone_dessin.create_rectangle(3*r, 4*r, 11*r, 6*r, outline="#FFFF00", fill="#FFFF00", width='3')
    if zone_dessin.plateau.gains_jaunes1>zone_dessin.plateau.gains_jaunes2:
        zone_dessin.create_text(7*r,5*r,text=('Joueur','1','a','gagné'),fill=('black'),font='Calibri')
        zone_dessin.create_text(2*r,10*r,text=('Joueur','1','a','gagné'),fill=('black'))
    elif zone_dessin.plateau.gains_jaunes2>zone_dessin.plateau.gains_jaunes1:
        zone_dessin.create_text(7*r,5*r,text=(plateau.mode_jeu,'a','gagné'),fill=('black'),font='calibri')
        zone_dessin.create_text(2*r,10*r,text=(plateau.mode_jeu,'a','gagné'),fill=('black'))

    else:
        zone_dessin.create_text(7*r,5*r,text=('Égalité'),fill=('Black'),font='Calibri')
        zone_dessin.create_text(2*r,10*r,text=('Égalité'),fill=('black'))


def dernier_pion_jouer(zone_dessin):    # Encadre en rouge le dernier pion joué sur le plateau.
    if plateau.joueur==1 and len(zone_dessin.plateau.pions_joueur_1)>2:
        zone_dessin.create_oval((zone_dessin.plateau.pions_joueur_2[-1][0]+2.1)*r,(zone_dessin.plateau.pions_joueur_2[-1][1]+1.1)*r,(zone_dessin.plateau.pions_joueur_2[-1][0]+2.9)*r,(zone_dessin.plateau.pions_joueur_2[-1][1]+1.9)*r, outline="red",width="4", fill=None)
    elif plateau.joueur==2 and len(zone_dessin.plateau.pions_joueur_1)>2:
        zone_dessin.create_oval((zone_dessin.plateau.pions_joueur_1[-1][0]+2.1)*r,(zone_dessin.plateau.pions_joueur_1[-1][1]+1.1)*r,(zone_dessin.plateau.pions_joueur_1[-1][0]+2.9)*r,(zone_dessin.plateau.pions_joueur_1[-1][1]+1.9)*r, outline="red",width="4", fill=None)


def dessiner_pions_yellow(zone_dessin):#Dessine les pions capturés en jaune et crée une animation pour les derniers pions capturés,effectue une transition visuelle pour la suppression des pions jaunes capturés du plateau de jeu.
    if zone_dessin.plateau.pions_yellow!=[]:
        if zone_dessin.liste_coup_jouer[-1][2]==0:
            for coordonees in zone_dessin.plateau.pions_yellow:
                zone_dessin.create_oval((coordonees[0]+2.1)*r,(coordonees[1]+1.1)*r,(coordonees[0]+2.9)*r,(coordonees[1]+1.9)*r, outline="yellow",width="3", fill="yellow")
            x,y=zone_dessin.plateau.pions_yellow[-1]
            zone_dessin.create_oval((x+2.1)*r,(y+1.1)*r,(x+2.9)*r,(y+1.9)*r, outline="yellow",width="3", fill="yellow")

 
def tout_dessiner(zone_dessin):#tout_dessiner est composée de tout_dessiner et tout_dessiner2 qui sont appelées selon mode de jeu: tout_dessiner pour le jeu contre l'ordinateur et tout_dessiner2 pour le jeu à 2 joueur

    zone_dessin.delete(tk.ALL)
    zone_dessin.pack(side=tk.TOP)

    plateau = zone_dessin.plateau
    joueur = plateau.joueur
    liste_coup_jouer=zone_dessin.liste_coup_jouer
    nbr=len(plateau.lister_coups_possibles(plateau.joueur)) # La variable nbr calcule le nombre de coups encore possibles pour le joueur courant, si celui ci atteind 0, la fin de partie se déclenche, l'ordinateur ne peux plus jouer et les fonctions liées au clic souris ne sont plus actives

    # Le paragraphe suivant est destiné au dessin de l'interface
    # D'abord le texte
    if nbr!=0:
        if plateau.joueur==1:
            zone_dessin.create_text(3*r,10*r,text=('Tour','de','Joueur',joueur),fill=('black'), font='calibri' )
        else:
            zone_dessin.create_text(2*r,10*r,text=('Tour','de',"l'Ordinateur"),fill=('black'),font='calibri')

    zone_dessin.create_text(4*r,r//2,text=('Score','Joueur','=',zone_dessin.plateau.gains_jaunes1),fill=('black'),font="calibri")
    zone_dessin.create_text(10*r-r//4,r//2,text=('Score',plateau.mode_jeu,'=',zone_dessin.plateau.gains_jaunes2),fill=('black'),font="calibri")
    zone_dessin.create_oval(2.25*r,r//4,2.25*r+r//2,3*r//4, outline="green",width="4", fill="green")
    zone_dessin.create_oval(7.25*r+r//2,r//4,8.25*r,3*r//4, outline="#00BFFF",width="4", fill="#00BFFF")


    # Ensuite la grille
    for i in range (8):
      for j in range (10):
        x1 = j*r + 2*r
        y1 = i*r + r
        x2 = x1 + r
        y2 = y1 + r
        zone_dessin.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
    # Puis les pions
    for coordonees in zone_dessin.plateau.pions_joueur_1:
        zone_dessin.create_oval((coordonees[0]+2.1)*r,(coordonees[1]+1.1)*r,(coordonees[0]+2.9)*r,(coordonees[1]+1.9)*r, outline="green",width="3", fill="green")
    for coordonees in zone_dessin.plateau.pions_joueur_2:
        zone_dessin.create_oval((coordonees[0]+2.1)*r,(coordonees[1]+1.1)*r,(coordonees[0]+2.9)*r,(coordonees[1]+1.9)*r, outline="#00BFFF",width="3", fill="#00BFFF")

    dessiner_pions_yellow(zone_dessin)

    if nbr!=0:
        dernier_pion_jouer(zone_dessin)

    # Et les croix grises pour les coups possibles
    dessiner_coups_possibles(zone_dessin,plateau.lister_coups_possibles(plateau.joueur))

    # Et enfin le cadre de fin de partie
    if nbr==0:
        fin_de_partie(zone_dessin)

    # Les prochaines lignes décrivent le jeu de l'ordinateur, d'abord on prend un coup aléatoire dans les coups qui lui sont possibles, s'il y a des coups qui font des gains on choisit les plus gros gains (pour cela on regarde parmi tous les voisins les pions du joueur adverse et on calcule le nombre de pions jaunes si on ajoute le pion de l'ordinateur), sinon on se place sur un voisin indirect d'un pion jaune et si aucun des deux derniers cas ne se présente, on conserve le coup aléatoire.

    if plateau.joueur==2 and nbr!=0:
        coup_ordi=random.randint(0,len(plateau.lister_coups_possibles(plateau.joueur))-1)
        xp,yp=plateau.lister_coups_possibles(plateau.joueur)[coup_ordi]
        possibilité_de_jaunir_des_pions=0
        for coup in plateau.lister_coups_possibles(plateau.joueur):
            pions_a_jaunir=[]
            pions=[]
            nombre_voisins_joueur=0
            tous_les_voisins=[(coup[0],coup[1]-1),(coup[0]-1,coup[1]),(coup[0],coup[1]+1),(coup[0]+1,coup[1]),(coup[0]-1,coup[1]-1),(coup[0]-1,coup[1]+1),(coup[0]+1,coup[1]-1),(coup[0]+1,coup[1]+1)]
            for x in tous_les_voisins:
                if Coup(x[0],x[1],plateau,plateau.joueur).est_dans_la_grille()==True:
                    if plateau.grille.get(x[0],x[1])==1:
                        pions.append((x[0],x[1]))
            for coord in pions:
                tous_les_voisins_coord=[(coord[0],coord[1]-1),(coord[0]-1,coord[1]),(coord[0],coord[1]+1),(coord[0]+1,coord[1]),(coord[0]-1,coord[1]-1),(coord[0]-1,coord[1]+1),(coord[0]+1,coord[1]-1),(coord[0]+1,coord[1]+1)]
                nombre_voisins_joueur=0
                for x in tous_les_voisins_coord:
                    if Coup(x[0],x[1],plateau,plateau.joueur).est_dans_la_grille()==True:
                        if plateau.grille.get(x[0],x[1])==2:
                            nombre_voisins_joueur+=1
                if nombre_voisins_joueur==3:    #Le prochain pion placé sera le quatrième necessaire au gain d'un pion jaune
                    pions_a_jaunir.append((coord[0],coord[1]))
            if  len(pions_a_jaunir)>possibilité_de_jaunir_des_pions:
                possibilité_de_jaunir_des_pions=len(pions_a_jaunir)
                xp,yp=coup[0],coup[1]
        if possibilité_de_jaunir_des_pions==0:
            for coup in plateau.lister_coups_possibles(plateau.joueur):
                voisins_indirects=[(coup[0]-1,coup[1]-1),(coup[0]-1,coup[1]+1),(coup[0]+1,coup[1]-1),(coup[0]+1,coup[1]+1)]
                for x,y in voisins_indirects:
                    if Coup(x,y,plateau,plateau.joueur).est_dans_la_grille():
                        if plateau.grille.get(x,y)==3:
                            xp,yp=coup[0],coup[1]

        zone_dessin.plateau.pions_joueur_2.append((xp,yp))  #On met à jour les pions de l'ordinateur
        plateau.grille.set(xp,yp,2) #On met a jour la grille
        plateau.joueur=1    #On change de joueur
        zone_dessin.liste_coup_jouer.append((xp,yp,0))          #On initialise le nombre de pions jaunes gagnés à 0 et celui sera mis à jour lors de l'utilisation de la méthode lister_pions_a_jaunir
        zone_dessin.xp=zone_dessin.liste_coup_jouer[-1][0]       #On retient la coordonnée pour la méthode DEFAIRE
        zone_dessin.yp=zone_dessin.liste_coup_jouer[-1][1]       #On retient la coordonnée pour la méthode DEFAIRE
        zone_dessin.coup=Coup(xp,yp,plateau,plateau.joueur)
        if zone_dessin.coup!=None:
            zone_dessin.coup.jaunir_pions_de_liste(zone_dessin.coup.lister_pions_a_jaunir())
        zone_dessin.coup=None
        tout_dessiner(zone_dessin)

    #La suite est destiné au jeu du joueur
    def case_cliquee(event):
        if plateau.joueur==1:
            xp=(event.x-2*r)//r
            yp=(event.y-r)//r

            if Coup(xp,yp, plateau, plateau.joueur).est_dans_la_grille()==True: #si le coup est dans la grille on crée un petit cadre rouge
                for k in range (2):
                    zone_dessin.create_line((xp+k)*r+2*r,yp*r+r,(xp+k)*r+2*r,(yp+1)*r+r, fill='#fff000800',width='2')
                    zone_dessin.create_line((xp+2)*r,(yp+k)*r+r,(xp+3)*r,(yp+k)*r+r, fill='#fff000800',width='2')
            if Coup(xp,yp, plateau, plateau.joueur).est_valide()==True:
                zone_dessin.plateau.pions_joueur_1.append((xp,yp))  #On met à jour les pions du joueur
                plateau.grille.set(xp,yp,1) #On met a jour la grille
                plateau.joueur=2    #On change de joueur

                zone_dessin.liste_coup_jouer.append((xp,yp,0))
                zone_dessin.xp=zone_dessin.liste_coup_jouer[-1][0] #On retient la coordonnées pour la méthode DEFAIRE
                zone_dessin.yp=zone_dessin.liste_coup_jouer[-1][1] #On retient la coordonnées pour la méthode DEFAIRE

            elif Coup(xp,yp, plateau, plateau.joueur).est_dans_la_grille()==True and Coup(xp,yp, plateau, joueur).est_valide()==False:  #Si le coup n'est pas valide on dessine une croix rouge
                zone_dessin.create_line((xp+2)*r,yp*r+r,(xp+3)*r,(yp+1)*r+r, fill='red',width='2')
                zone_dessin.create_line((xp+3)*r,(yp)*r+r,(xp+2)*r,(yp+1)*r+r, fill='red',width='2')

            zone_dessin.coup=Coup(xp,yp,plateau,plateau.joueur)
            if zone_dessin.coup!=None:
                zone_dessin.coup.jaunir_pions_de_liste(zone_dessin.coup.lister_pions_a_jaunir())
            zone_dessin.coup=None

    def case_relachee(event):
        tout_dessiner(zone_dessin)

    if zone_dessin.liste_coup_jouer!=[]:   #S'il y a au moins un coup joué on active le bouton DEFAIRE
        bouton_defaire["state"]=tk.NORMAL
    else:
        bouton_defaire["state"]=tk.DISABLED
    zone_dessin.bind('<Button-1>', case_cliquee)
    zone_dessin.bind('<ButtonRelease-1>', case_relachee)

#La fonction tout_dessiner2 est très similaire

def tout_dessiner2(zone_dessin):
    zone_dessin.delete(tk.ALL)
    zone_dessin.pack(side=tk.TOP)

    plateau = zone_dessin.plateau
    joueur = plateau.joueur
    liste_coup_jouer=zone_dessin.liste_coup_jouer
    nbr=len(plateau.lister_coups_possibles(plateau.joueur))

    #On dessine l'interface
    zone_dessin.create_text(7*r,10*r,text=('Tour','du','Joueur',joueur),fill=('black'), font="calibri")
    zone_dessin.create_text(4*r,r//2,text=('Score','Joueur','1','=',zone_dessin.plateau.gains_jaunes1),fill=('black'),font="calibri")
    zone_dessin.create_text(10*r,r//2,text=('Score','Joueur','2','=',zone_dessin.plateau.gains_jaunes2),fill=('black'),font="calibri")
    zone_dessin.create_oval(2*r,r//4,2*r+r//2,3*r//4, outline="green",width="3", fill="green")
    zone_dessin.create_oval(11*r+r//2,r//4,12*r,3*r//4, outline="#00BFFF",width="3", fill="#00BFFF")

    for i in range (8):
      for j in range (10):
        x1 = j*r + 2*r
        y1 = i*r + r
        x2 = x1 + r
        y2 = y1 + r
        zone_dessin.create_rectangle(x1, y1, x2, y2, outline="black", fill="WHITE")
    for coordonees in zone_dessin.plateau.pions_joueur_1:
        zone_dessin.create_oval((coordonees[0]+2.1)*r,(coordonees[1]+1.1)*r,(coordonees[0]+2.9)*r,(coordonees[1]+1.9)*r, outline="green",width="3", fill="green")
    for coordonees in zone_dessin.plateau.pions_joueur_2:
        zone_dessin.create_oval((coordonees[0]+2.1)*r,(coordonees[1]+1.1)*r,(coordonees[0]+2.9)*r,(coordonees[1]+1.9)*r, outline="#00BFFF",width="3", fill="#00BFFF")

    dessiner_pions_yellow(zone_dessin)

    if nbr!=0:
        dernier_pion_jouer(zone_dessin)

    dessiner_coups_possibles(zone_dessin,plateau.lister_coups_possibles(plateau.joueur))

    if nbr==0:
        fin_de_partie(zone_dessin)
    #Tout se fait en fonction de la case cliquée et les joueurs s'altèrnent
    def case_cliquee(event):
        xp=(event.x-2*r)//r
        yp=(event.y-r)//r
        if nbr!=0:  #Condition qui permet de plus pouvoir modifier la grille par un clic après la fin de partie
            if Coup(xp,yp, plateau, plateau.joueur).est_dans_la_grille()==True:
                for k in range (2):
                    zone_dessin.create_line((xp+k)*r+2*r,yp*r+r,(xp+k)*r+2*r,(yp+1)*r+r, fill='#fff000800',width='2')
                    zone_dessin.create_line((xp+2)*r,(yp+k)*r+r,(xp+3)*r,(yp+k)*r+r, fill='#fff000800',width='2')
            if Coup(xp,yp, plateau, plateau.joueur).est_valide()==True:
                if joueur==1:
                    zone_dessin.plateau.pions_joueur_1.append((xp,yp))
                    plateau.grille.set(xp,yp,1)
                    plateau.joueur=2
                else:
                    zone_dessin.plateau.pions_joueur_2.append((xp,yp))
                    plateau.grille.set(xp,yp,2)
                    plateau.joueur=1
                zone_dessin.liste_coup_jouer.append((xp,yp,0))
                zone_dessin.xp=zone_dessin.liste_coup_jouer[-1][0] #On retient la coordonnées pour la méthode DEFAIRE
                zone_dessin.yp=zone_dessin.liste_coup_jouer[-1][1] #On retient la coordonnées pour la méthode DEFAIRE

            elif Coup(xp,yp, plateau, plateau.joueur).est_dans_la_grille()==True and Coup(xp,yp, plateau, joueur).est_valide()==False:
                zone_dessin.create_line((xp+2)*r,yp*r+r,(xp+3)*r,(yp+1)*r+r, fill='black',width='2')
                zone_dessin.create_line((xp+3)*r,(yp)*r+r,(xp+2)*r,(yp+1)*r+r, fill='black',width='2')

        zone_dessin.coup=Coup(xp,yp,plateau,plateau.joueur)
        if zone_dessin.coup!=None:
            zone_dessin.coup.jaunir_pions_de_liste(zone_dessin.coup.lister_pions_a_jaunir())
        zone_dessin.coup=None

    def case_relachee(event):
        tout_dessiner2(zone_dessin)

    if zone_dessin.liste_coup_jouer!=[]:
        bouton_defaire["state"]=tk.NORMAL
    else:
        bouton_defaire["state"]=tk.DISABLED
    zone_dessin.bind('<Button-1>', case_cliquee)
    zone_dessin.bind('<ButtonRelease-1>', case_relachee)

#Définition de l'environnement tkinter

fenetre = tk.Tk()
fenetre.title('Quathello')

frame_top = tk.Frame(fenetre)
frame_top.pack(anchor=tk.NW)
zone_dessin=tk.Canvas(fenetre, bg= "#F5F5F5", width=14*r, height=12*r) 

button = tk.Button(frame_top, text="QUITTER", fg="red", bg="white" , command=fenetre.destroy)
button.pack(side=tk.LEFT)

bouton_defaire = tk.Button(frame_top, text="DEFAIRE", fg="red", bg='white', state=tk.DISABLED, command=lambda: CoupJoue(zone_dessin.xp,zone_dessin.yp,zone_dessin.plateau.pions_yellow).defaire(zone_dessin.plateau))
bouton_defaire.pack(side=tk.RIGHT)

bouton_restart = tk.Button(frame_top, text="Nouvelle partie", command=lambda: nouvelle_partie(zone_dessin), fg="black",bg='white')
bouton_restart.pack(side=tk.BOTTOM)

bouton_mode_de_jeu = tk.Button(frame_top, text=('Modifier', 'Mode', 'de', 'Jeu'), command=lambda: mode_de_jeu(zone_dessin), fg="black",bg='white')

bouton_mode_de_jeu.pack(side=tk.BOTTOM)

#Initialisation des variables stockées en attribut dans zone_dessin

def mode_de_jeu(zone_dessin):
    if plateau.mode_jeu=='Ordinateur':
        plateau.mode_jeu='Joueur_2'
    else:
        plateau.mode_jeu='Ordinateur'
    nouvelle_partie(zone_dessin)

#Pour chaque nouvelle partie on réinitialise toutes les valeurs
def nouvelle_partie(zone_dessin):
    for i in range (8):
      for j in range (10):
          plateau.grille.set(j,i,0)
    plateau.placer_pions()
    plateau.joueur=1
    zone_dessin.plateau = plateau
    zone_dessin.plateau.gains_jaunes1=0
    zone_dessin.plateau.gains_jaunes2=0
    zone_dessin.liste_coup_jouer=[]
    zone_dessin.plateau.pions_joueur_1=[(4,4),(5,3)]
    zone_dessin.plateau.pions_joueur_2=[(4,3),(5,4)]
    zone_dessin.plateau.pions_yellow=[]

    if plateau.mode_jeu=='Ordinateur':
        tout_dessiner(zone_dessin)
    else:
        tout_dessiner2(zone_dessin)
    return zone_dessin.plateau


#Execution du programme final

nouvelle_partie(zone_dessin)


fenetre.mainloop()