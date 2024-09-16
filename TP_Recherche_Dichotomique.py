def recherche_dichotomique(tab, v):
    debut = 0
    fin = len(tab)-1
    ind = -1
    count = 0
    while ind == -1 and debut <= fin:
        count = count + 1
        milieu = (debut + fin)//2
        if tab[milieu] == v:
            ind = milieu
        elif tab[milieu] < v:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return (ind, count)

def genere_tableau(maxi):
    t = [i for i in range(1, maxi+1)]
    return t