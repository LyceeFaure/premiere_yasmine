def racine(x : float) -> float:
    ''' Calculer la racine carrée de a
    '''
    assert x >=0, "Il faut que le nombre entré soit supérieur ou égal à 0"
    y = 1
    for i in range(10):
        y = (y+x/y)/2
    return y
    assert y >=0,"IL faut que le nombre sorti soit supérieur ou égal à 0"
assert round(racine(4)) == 2,"Erreur pour la valeur 4"     
assert round(racine(9)) == 3,"Erreur pour la valeur 9"    
assert round(racine(36)) == 6,"Erreur pour la valeur 36"