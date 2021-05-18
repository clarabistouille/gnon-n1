from turtle import *
from mazelib import Maze
from mazelib.generate.Prims import Prims
import random

speed(0)
tracer(1000)

noir = "#211C1D"
vert = "#06EFB1"
rouge = "#FE5D62"
bleu = "#70C3FF"
jaune = "#FFD485"

def rectangle(long : int, larg : int, x : int, y : int):
    up()
    goto(x, y)
    down()
    forward(long)
    right(90)
    forward(larg)
    right(90)
    forward(long)
    right(90)
    forward(larg)
    right(90)

def color_carre(couleur : str, x : int, y : int):
    color(noir, couleur)
    begin_fill()
    rectangle(50, 50, x, y)
    end_fill()

register_shape("piece.gif")
register_shape("méchant(1).gif")

def dessine_bonom(x, y, carte_bonom):
    if carte_bonom[y][x] == "P":
        shape("piece.gif")

        up()
        goto(-300 + 50 * x + 25, 300 - 50 * y - 25)
        carte_bonom[y][x] = stamp()
        down()

    elif carte_bonom[y][x] == "M":
        shape("méchant(1).gif")

        up()
        goto(-300 + 50 * x + 25, 300 - 50 * y - 25)
        carte_bonom[y][x] = stamp()
        down()

    update()


def construire_carte(carte, carte_bonom):
    x = -300
    y = 300

    for ligne in carte:
        for cellule in ligne:
            if cellule == "eau":
                color_carre(bleu, x, y)
            elif cellule == "lave":
                color_carre(rouge, x, y)
            elif cellule == "herbe":
                color_carre(vert, x, y)
            x = x + 50
        y = y - 50
        x = -300

    x = -300
    y = 300

    for i in range(11):
        for j in range(11):
            dessine_bonom(i, j, carte_bonom)
            x = x + 50
        y = y + 50
        x = -300

def labyrinthe(carte, case_init, case_fin):
    lab = Maze()
    lab.start = case_init
    lab.end = case_fin
    lab.generator = Prims(6, 6)
    lab.generate()
    n = random.randint(0,1)
    for i in range(11):
        for j in range(11):
            if lab.grid[i + 1][j + 1] == 1:
                if n == 0:
                    carte[i][j] = "eau"
                else:
                    carte[i][j] = "lave"
            else:
                carte[i][j] = "herbe"

def est_croisement(carte, x, y):
    if (x == 0 or y == 0 or x == 10 or y == 10 or carte[y][x] != "herbe"):
        return False
    else:
        cases = []
        compteur = 0
        cases.append(carte[y - 1][x])
        cases.append(carte[y + 1][x])
        cases.append(carte[y][x + 1])
        cases.append(carte[y][x - 1])
        for case in cases:
            if case == "herbe":
                compteur += 1
        return (compteur > 2)

def est_culdesac(carte, x, y):
    if carte[y][x] != "herbe":
        return False
    compteur = 0
    cases = []
    if x == 0:
        compteur += 1
        cases.append(carte[y][x + 1])
    elif x == 10:
        compteur += 1
        cases.append(carte[y][x - 1])
    else:
        cases.append(carte[y][x - 1])
        cases.append(carte[y][x + 1])
    if y == 0:
        compteur += 1
        cases.append(carte[y + 1][x])
    elif y == 10:
        compteur += 1
        cases.append(carte[y - 1][x])
    else:
        cases.append(carte[y + 1][x])
        cases.append(carte[y - 1][x])
    for case in cases:
        if case == "lave" or case == "eau":
            compteur += 1
    return (compteur == 3)

def pose_bonom(carte, carte_bonom):
    for i in range(11):
        for j in range(11):
            if est_croisement(carte, j, i):
                carte_bonom[i][j] = "M"
            elif est_culdesac(carte, j, i):
                carte_bonom[i][j] = "P"

def init_carte(carte, carte_bonom):
    """
    on crée la carte sous forme de liste de liste.
    chaque cellule contient un string qui defini l'état de la cellule de la carte
    """
    for i in range(11):
        ligne = []
        ligne_b = []
        for j in range(11):
            ligne.append("lave")
            ligne_b.append("-")
        carte.append(ligne)
        carte_bonom.append(ligne_b)
    labyrinthe(carte, (0, 0), (10, 10))
    pose_bonom(carte, carte_bonom)
    construire_carte(carte, carte_bonom)
    update()
