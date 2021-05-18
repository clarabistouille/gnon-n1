from turtle import *

def dessine_psg(psg):
    register_shape("poti-mario.gif")
    shape("poti-mario.gif")
    resizemode("user")
    shapesize(1, 1, 12)

    up()
    x = psg["position"][0]
    y = psg["position"][1]
    x_psg = -300 + 50 * x + 25
    y_psg = 300 - 50 * y - 25
    goto(x_psg, y_psg)
    psg["curseur"] = stamp()
    update()

def maj_etat_psg(carte, psg, position):
    """
    met à jour les informations du personnage en fonction des aléas rencontrés sur la case
    """
    case = carte[position[1]][position[0]]
    if case == "lave":
        psg["vie"] = 0
    elif case == "eau":
        psg["vie"] -= 5
    psg["position"] = position
