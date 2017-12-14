## CHECK PATH

# Este programa actualizara un archivo con los datos de las centrales
from dataTranslate import uhourCents ## Importar la funcion que dara la información sobre todas las centrales

def updateInfoWeb(): ## Se define una funcion que va a escribir en el archivo infoWeb.txt, la informacion para cada central en una fila distinta
    file = open ("./files/infoWeb.txt","w") # Abrir el archivo
    matrix = uhourCents() # definir una lista igual a la informacion que de la funcion uhourCents
    global string
    string = "" # cadena de caracteres vacia donde se guardara la informacion
    for x in matrix:
        string = string + str(x) + "\n"
    file.write(string) # escribir en el archivo la informacion