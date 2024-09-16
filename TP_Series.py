import csv

#ouverture du fichier csv
def lecture_fichier(nom_fichier):
    with open(nom_fichier, mode='r') as fichier_ouvert:
        return list(csv.reader(fichier_ouvert,delimiter=","))

def exporte(tableau, nom_fichier):
    fichier = open(nom_fichier, "w",newline='')
    writer = csv.writer(fichier)
    writer.writerows(tableau)
    
def fusionne(table1, table2):
    return table1 + table2[1:]
    
def trouve_doublons(table):
    doublons = []
    for i in range(1, len(table)):
        for j in range(i+1, len(table)):
            if ...:
                doublons.append(...)
    return doublons

def supprime_doublons(table):
    for i in range(len(table)-1, ..., ...):
        for j in range(len(table)-1, i, -1):
            if ...:
                ...
    return table


def tri_caracteres(table, colonne):
    for i in range(2,len(table)):
        valeur = table[i]
        j = i
        while j>1 and valeur[colonne] < table[j-1][colonne]:
            table[j] = table[j-1]
            j -= 1
        if j!=i:
            table[j] = valeur
            
def tri_nombres(table, colonne):
    for i in range(2,len(table)):
        valeur = table[i]
        j = i
        while j>1 and ...:
            table[j] = table[j-1]
            j -= 1
        if j!=i:
            table[j] = valeur
        

# Faire les appels de fonctions ci-dessous
serie_1 = lecture_fichier("series_1.csv")
serie_2 = lecture_fichier("series_2.csv")
series = fusionne("series_1.csv", "series_2.csv")