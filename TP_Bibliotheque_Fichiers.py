from random import randint

nombre_mystere = randint(0,100)
nombre = 1
nb_essais = 0
    
while nombre != nombre_mystere and nb_essais < 10:
    nombre = int(input("Entrez un nombre : "))
    nb_essais = nb_essais + 1
    
    if nombre > nombre_mystere:
        print ("Le nombre est inférieur")
    elif nombre < nombre_mystere:
        print ("Le nombre est supérieur")
    else:
        print ("Vous avez trouvé en " + str(nb_essais))
    if nb_essais == 10:
        print ("Vous avez perdu")