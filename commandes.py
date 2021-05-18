def avance(carte, x, y):
    if y == 0:
        return (-1, -1)
    return (x, y - 1)

def recule(carte, x, y):
    if y == 10:
        return (-1, -1)
    return (x, y + 1)
    
def droite(carte, x, y):
    if x == 10:
        return (-1, -1)
    return (x + 1, y)
    
def gauche(carte, x, y):
    if x == 0:
        return (-1, -1)
    return (x - 1, y)
    
def init_commandes(commandes):
    commandes.append("h")
    commandes.append("b")
    commandes.append("d")
    commandes.append("g")
    commandes.append("help")
