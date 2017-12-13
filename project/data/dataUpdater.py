## Este programa se encargara de actualizar los archivos, ejecutando las funciones de los otros programas
## matS.py se corre en paralelo
import time
import datetime
from dataGet import updateData
from dataTranslate import actualMata

lastHour = datetime.datetime.today().hour
updateData()
actualMata()

while True:
    
    if datetime.datetime.today().hour == 0: ## Cuando sean las 12
        
        updateData() ## Descargar la informacion de la pagina web y guardarla en un archivo
        time.sleep(5) ## Esperar 5 segundos
        actualMata()
        
    else:
        
        if datetime.datetime.today().hour is not lastHour:
            
            actualMata()
            lastHour = datetime.datetime.today().hour # Igualar ultima hora leida a la hora leida en cada ciclo
            time.sleep(5) # Esperar 5 segundos
        
        else:
            
            time.sleep(5) # Si todavia no ha cambiado la hora, esperar 5 segundos
