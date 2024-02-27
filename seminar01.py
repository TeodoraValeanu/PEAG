#Functie care primeste un vector si afiseaza fiecare element din vector invers
#231 - > 132
#12 - > 21
#2 -> 2
#30 -> 3

#Eliminarea duplicatelor dintr-un vector


def mirrorElement(n):
    result=0
    while n>0:
        result*=10
        result+=n%10
        n = int(n/10)

    return result

def rev(vector):
    newVector=[]
    for iterator in vector:
        newVector.append(mirrorElement(iterator))
    return newVector
def stergeDubluri(vector):
    vazute = []
    rez = []
    for i in vector:
        if i not in vazute:
            rez.append(i)
            vazute.append(i)
    return rez

vect=[10, 123, 35, 46, 46, 23, 35]

print(rev(vect))
print(stergeDubluri(vect))




