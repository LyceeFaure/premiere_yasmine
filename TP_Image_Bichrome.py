from matplotlib.pyplot import *

image = [ [0 for i in range(25)] for j in range(25)]
for i in range(len(image)):
    for j in range(len(image[0])):
        if ((i==0 or j==0 or i==24 or j==24) or (i==12 or j==12)):
            image[i][j] = 1

imshow(image)
show()
