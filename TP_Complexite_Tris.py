from time import time

def minimum(t:list, debut: int) -> int:
    ind = debut
    for i in range(debut, len(t)):
        if t[ind] > t[i]:
            ind = i
    return ind
            
def echange(t: list, ind1: int, ind2: int) -> list:
    elt1 = t[ind1]
    t[ind1] = t[ind2]
    t[ind2] = elt1
    return t

def tri_selection(t:list) -> list:
    for i in range(len(t)-1):
        min_ind = minimum(t,i)
        if i != min_ind:
            t = echange(t,i,min_ind)
    return t

def tri_insertion(t:list) -> list:
    for i in range(1, len(t)):
        val_i = t[i]
        j = i
        while j > 0 and val_i < t[j-1]:
            t[j] = t[j-1]
            j = j-1
        if j != i:
            t[j] = val_i
    return t

t1 = [200-i for i in range(200)]
t2 = [400-i for i in range(400)]
t3 = [600-i for i in range(600)]
t4 = [800-i for i in range(800)]
t5 = [1000-i for i in range(1000)]

i1 = [200-i for i in range(200)]
i2 = [400-i for i in range(400)]
i3 = [600-i for i in range(600)]
i4 = [800-i for i in range(800)]
i5 = [1000-i for i in range(1000)]

tp1 = [i for i in range(200)]
tp2 = [i for i in range(400)]
tp3 = [i for i in range(600)]
tp4 = [i for i in range(800)]
tp5 = [i for i in range(1000)]

debut = time()
tri_insertion(tp5)
tps = (time()-debut)*1000