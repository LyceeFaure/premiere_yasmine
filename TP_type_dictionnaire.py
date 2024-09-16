dico = {}
dico["nom"] = "Lennon"
dico["prénom"] = "John"
dico["année de naissance"] = 1940

for k in dico.keys():
    print(k)
    
dictionnaire = {"clé1": "valeur1", "clé2": "valeur2"}
dico2 = {"nom": "McCartney", "pénom": "Paul", "année de naissance": 1942}

exif = {"largeur": "4592 pixels", "hauteur": "2584 pixels"}

rockband = {"chanteur": "Julian Casablancas", "guitariste rythmique": "Albert Hammond Jr", "lead guitariste": "Nick Valensi", "bassiste": "Nikolai Fraiture", "batteur": "Fabrizio Moretti"}

def est_membre(rockband, nom):
    for v in range(len(rockband)):
        if nom == v:
            return True
        else:
            return False