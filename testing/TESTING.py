import random
file = open ("testing.txt")
file2 = open ("testing2.txt")
global string
string = ""
"""
length = (len(file.readlines()))
file = open ("testing.txt")
"""
"""
for x in file:
    string = string + "\"" + x.replace("\n", "") + "\"" + " , "
string = string + " ]"
file = open ("testing.txt", "w")
file.write(string)
"""
"""
for x in file:
    string = string + x.replace(",", " , ").replace("=", " = ")

file = open ("testing.txt", "w")
file.write(string)
"""
"""
matrix = [[0]*8 for x in range(0,8)]
for x in range(0,8):
    for y in range(0,8):
         matrix[x][y] = random.randint(0,1)

def from88to87mat(mat): ## Transforma la matriz de entrada 8*8 a una matriz de 8*7 y se devuelve
    longMat = []
    for x in range(0,8):
        for y in range(0,8):
            longMat.append(mat[x][y])

    the87mat = []

    for x in range(0,8):

        phmat = []

        for y in range(0,7):
            phmat.append(longMat[y+x*7])

        the87mat.append(phmat)

    return the87mat

print (matrix)
print ("\n")
print (from88to87mat(matrix))
"""
"""
string = ""
for x in file:
    string = string + x.replace("\n", " , ")

file = open ("testing.txt", "w")
file.write(string)
"""
"""
string = ""
for x in file:
    string = string + "$" + x.replace("\n", "") + " = fgets($file);\nf"

file = open ("testing.txt", "w")
file.write(string)
"""

string = ""
for y in file:
        string = string + y.replace("\n", "").replace( ")",");") + "\n"


file = open ("testing.txt", "w")
file.write(string)