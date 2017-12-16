## Este programa se encargara de actualizar los archivos, ejecutando las funciones de los otros programas
## matS.py se corre en paralelo junto con este

import time # para esperar un tiempo
import datetime # para saber la hora y el dia
from dataGet import updateData # para descargar la informacion del sitio
from dataTranslate import actualMata # para actualizar el archivo leido por matS.py
from infoWeb import updateInfoWeb # para actualizar el archivo que puede ser leido por la pagina web

global lastDay,lastHour # variable de tipo boolean que dice si ya se actualizo el archivo downData para el dia de hoy

lastDay = datetime.date.today().day # el dia
lastHour = datetime.datetime.today().hour # definir una variable lastHour igual a la hora en que se empiece a ejecutar el programa
updateData() # descargar los datos de la pagina
actualMata() # actualizar el archivo leido por matS.py
updateInfoWeb() # actualizar el archivo infoWeb


while True:

    if lastDay is not datetime.date.today().day: ## Cuando cambie el dia, es decir cuando sean las 12
        
        updateData() ## Descargar la informacion de la pagina web y guardarla en un archivo
        time.sleep(5) ## Esperar 5 segundos
        actualMata() ## actualizar el archivo leido por matS.py
        time.sleep(5)
        updateInfoWeb() # actualizar el archivo infoWeb
        time.sleep(5)

        lastDay = datetime.date.today().day # Igualar ultimo dia leido al dia leido en el ciclo

    else:
        
        if lastHour is not datetime.datetime.today().hour: # Si cambia la hora
            
            actualMata()
            time.sleep(5)
            updateInfoWeb()
            time.sleep(5)

            lastHour = datetime.datetime.today().hour # Igualar ultima hora leida a la hora leida en cada ciclo
        
        else:
            
            time.sleep(5) # Si todavia no ha cambiado la hora, ni el dia, esperar 5 segundos antes de empezar denuevo el ciclo
