from carte import *
from commandes import *
from personnage import *
from turtle import *

def test_commande(carte, psg, case_suiv):
    """
    lit un commande
    - retourne True si la parti est toujours en cours
    - retourne False si la partie est finie, c'est-à-dire que le joueur a perdu ou gagné
    """
    if case_suiv[0] == -1 :
        print("tu es sorti.e de la carte, remets tes yeux en face de tes trous stp")
        return False
    else:
        maj_etat_psg(carte, psg, case_suiv)

        if psg["vie"] == 0:
            print("Tu es mort, rip.")
            return False
        clearstamp(psg["curseur"])
        dessine_psg(psg)
        if psg["position"] == (10, 10):
            print("yay, tu as gagné !")
            return False
        return True


carte = []
carte_bonom = []
commandes = []
psg = {"vie" : 10, "curseur" : None, "position" : (0, 0)}
jeu = True

init_carte(carte, carte_bonom)
init_commandes(commandes)
x = 0
y = 0
dessine_psg(psg)

def f_av():
    avance(carte, psg[position][0], psg[position][1])

def f_rec():
    recule(carte, psg[position][0], psg[position][1])
    
def f_dr():
    droite(carte, psg[position][0], psg[position][1])
    
def f_ga():
    (x_res, y_res) = gauche(carte, psg[position][0], psg[position][1])
    psg["position"][0] = x_res
    psg["position"][1] = y_res

onkeypress(f_av, "Up")
onkeypress(f_rec, "Down")
onkeypress(f_dr, "Left")
onkeypress(f_ga, "Right")
listen()

jeu = test_commande(carte, psg, com, commandes)
