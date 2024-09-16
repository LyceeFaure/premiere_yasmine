import csv

#ouverture du fichier csv
def lecture_fichier(nom_fichier):
    with open(nom_fichier, mode='r') as fichier_ouvert:
        return list(csv.reader(fichier_ouvert,delimiter=","))
    
def test_latitude(table):
    ''' recherche les informations sur les pays dont la latitude est inférieure à 0 et la longitude supérieure à 0 '''
    erreur = []
    for i in range(1, len(table)):
        if float(table[i][2]) > 90 or float(table[i][2]) < -90:
            erreur = erreur + [table[i]]
    return erreur

def test_longitude(table):
    ''' recherche les informations sur les pays dont la latitude est inférieure à 0 et la longitude supérieure à 0 '''
    erreur = []
    for i in range(1, len(table)):
        if float (table[i][2]) > 180 or float (table[i][2]) < -180:
            erreur = erreur + [table[i]]
    return erreur
    
def recherche_1(table):
    ''' recherche les informations sur les pays situés sur le continent nord américain '''
    selection = []
    for i in range(1, len(table)):
        if (table[i][5]) == "North America":
            selection = selection + [table[i]]
    return selection
    
def recherche_2(table):
    ''' recherche les informations sur les pays dont la latitude est inférieure à 0 '''
    selection = []
    for i in range(1, len(table)):
        if float(table[i][2]) < 0:
            selection = selection + [table[i]]
    return selection
    
    
def recherche_3(table):
    ''' recherche les informations sur les pays dont la latitude est inférieure à 0 et la longitude supérieure à 0 '''
    selection = []
    for i in range(1, len(table)):
        if float(table[i][2]) < 0 and float(table[i][3]) > 0:
            selection = selection + [table[i]]
    return selection

#import des données - question A.3
capitales = lecture_fichier("capitales.csv")
#vérification de la cohérence des données - partie B
test_latitude(capitales)
test_longitude(capitales)
# écrire les assertion vérifiant qu'on ne trouve pas de données avec des erreurs

#recherches dans les données - partie C

