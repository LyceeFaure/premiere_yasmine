from matplotlib.pyplot import *

image = [ [(0, 0, 0)for i in range(25)] for j in range(25)]

def carre_couleur(image,c):
    for i in range(len(image)):
        for j in range(len(image[0])):
            if i==0 or j==0 or i==24 or j==24:
                image[i][j] = image
            else:
                image[i][j] = c
    return image
            
imshow(image) 
show()