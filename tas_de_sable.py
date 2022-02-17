import tkinter
import random

M = []

######## création de la matrice carée de taille (size) voulue

def matrice(size): 
    matrice1 = []
    for i in range (0, size):
        matrice1.append([])
    return (matrice1)

######## définition de la matrice complète de taille (size) voulue

def configuration(size):
    L = matrice(size)
    for i in range (0, size):
        for j in range(0, size):
            L[j].append(random.randint(0,3))
    print(L)
    return L

####### addition de 2 configurations (m1 et m2) 

def addition(m1, m2):
    limit1 = len(m1)
    limit10 = len(m1[0])
    limit2 = len(m2)
    limit20 = len(m2[0])
    result_matrix = m1
    if (limit1) != (limit2) or (limit10) != (limit20):
        print("Tailles de matrices différentes")
        return -1
    else:
        for i in range (0,limit1):
            for j in range (0, limit10):
                result_matrix[i][j] += m2[i][j]
        print (result_matrix)
        return result_matrix

####### soustraction de 2 configurations (m1, m2)

def soustraction(m1, m2):
    limit1 = len(m1)
    limit10 = len(m1[0])
    limit2 = len(m2)
    limit20 = len(m2[0])
    result_matrix = m1
    if (limit1) != (limit2) or (limit10) != (limit20):
        print("Tailles de matrices différentes")
        return -1
    else:
        for i in range (0,limit1):
            for j in range (0, limit10):
                result_matrix[i][j] -= m2[i][j]
                if (result_matrix[i][j] < 0):
                    result_matrix[i][j] = 0
        print (result_matrix)
        return result_matrix

####### Max stable : Attribue 3 grains à toutes les cases de la matrice

def max_stable(L):
    limite1 = len(L)
    for i in range (0, limite1):
        for j in range (0, limite1):
            L[j].append(3)
    print(L)
    return L

####### Pile : attribue un grain à la case du milieu de la matrice et 0 aux autres

def pile(L):
    index1 = len(L)
    for i in range (index1):
        for j in range (index1):
            L[j].append(0)
    L[index1 // 2][index1 // 2] = 3
    print(L)

########## TESTS
print ("ex1 = ") 

ex1 = configuration(3)

print("ex2 = ")
        
ex2 = configuration(3)

print("soustraction = ")

soustraction(ex1, ex2)

print ("max stable = ")

max_stable(matrice(3))

print ("Pile = ")

pile(matrice(3))
