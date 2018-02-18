
## Revisar direccion path
path = "/home/pi/project/data/files/" ## Direccion de los archivos de texto

# Este programa actualizara un archivo de texto con los datos de las centrales ( generacion en MWh para cada central, una por cada linea, en el orden que se encuentra descrito en el archivo Centrales
## Esto se usara para la pagina web
from dataTranslate import uhourCents ## Del programa dataTranslate.py, Importar la funcion que dara la informacion sobre todas las centrales para la hora en que se ejecute la funcion

def updateInfoWeb(): ## Se define una funcion que va a escribir en el archivo infoWeb.txt, la informacion para cada central en una fila distinta
    
    matrix = uhourCents() # definir una lista igual a la informacion que devuelva la funcion uhourCents
    global string # variable string global
    string = "" # cadena de caracteres vacia donde se guardara la informacion
    for x in matrix: # Para cada elemento de matrix ( un valor de una central )
        string = string + str(x) + "\n" # Agregar a string, el valor, y un caracter 'newline' (\n) (Tiene el mismo resultado que presionar enter al escribir unr achivo de texto)

    file = open (path + "infoWeb.txt","w") # Abrir el archivo para escritura
    file.write(string) # Guardar la informacion de string en el archivo