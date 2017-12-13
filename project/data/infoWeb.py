# Este programa actualizara un archivo con los datos de las centrales
from dataTranslate import uhourCents

def updateInfoWeb():
    file = open ("./files/infoWeb.txt","w")
    matrix = uhourCents()
    global string
    string = ""
    for x in matrix:
        string = string + str(x) + "\n"
    file.write(string)