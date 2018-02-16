## Este programa se encargara de actualizar los archivos, ejecutando las funciones de los otros programas
## matS.py se corre en paralelo con este

import time ## Libreria usada para hacer que el programa se pause por un tiempo especifico (usando la funcion sleep de la libreria ( time.sleep(tiempo en segundos) ))
import datetime # Libreria usada para obtener dia y hora
from dataGet import updateData # del archivo dataGet.py, importar la funcion updateData, que para el dia de ejecucion, descarga la informacion de xm.com.co, y la guarda en downData.txt
from dataTranslate import actualMata # del archivo dataTranslate.py, importar la funcion actualMata, que al ser ejecutada, guarda un matriz, en el archivo matSdata.txt, con el estado de cada central para la hora de ejecucion
from infoWeb import updateInfoWeb # del archivo infoWeb.py, importar la funcion updateInfoWeb, que actualiza el archivo infoWeb con los datos de generacion de las centrales

global lastDay,lastHour # Variables que contendran el dia y la hora medidas por ultima vez

## Esta parte del codigo actualiza todos los archivos
lastDay = datetime.date.today().day # Obtener el dia para cuando se ejecute esta parte del codigo
lastHour = datetime.datetime.today().hour # Obtener la hora para cuando se ejecute esta parte del codigo
updateData() # Descargar informacion de xm.com.co ( actualizar downData.txt )
actualMata() # Actualizar el archivo leido por matS.py ( matSdata.txt )
updateInfoWeb() # Actualizar el archivo infoWeb.txt


while True:

    if lastDay is not datetime.date.today().day: ## Cuando cambie el dia, es decir cuando sean las 12 ( Si la ultima hora guardada, es diferente a la hora tomada en el tiempo de ejecucion de esta parte del codigo, significa que cambio la hora )
        
        updateData() # Descargar informacion de xm.com.co ( actualizar downData.txt )
        time.sleep(5) ## Esperar 5 segundos
        actualMata() # Actualizar el archivo leido por matS.py ( matSdata.txt )
        time.sleep(5) ## Esperar 5 segundos
        updateInfoWeb() # Actualizar el archivo infoWeb.txt
        time.sleep(5) ## Esperar 5 segundos

        lastDay = datetime.date.today().day # Actualizar el ultimo dia leido, al dia leido al ejecutar esta parte del codigo

    else:
        
        if lastHour is not datetime.datetime.today().hour: # Si cambia la hora
            
            actualMata() # Actualizar el archivo leido por matS.py ( matSdata.txt )
            time.sleep(5) ## Esperar 5 segundos
            updateInfoWeb() # Actualizar el archivo infoWeb.txt
            time.sleep(5) ## Esperar 5 segundos

            lastHour = datetime.datetime.today().hour # Igualar ultima hora leida a la hora leida en cada ciclo
        
        else:
            
            time.sleep(5) # Si todavia no ha cambiado la hora, ni el dia, esperar 5 segundos antes de comprar denuevo si hay un cambio
