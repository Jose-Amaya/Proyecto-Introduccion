## revisar direccion path
path = "/home/pi/project/data/files/" ## Direccion de los archivos de texto

import datetime # Libreria usada para obtener dia y hora
import time ## Libreria usada para hacer que el programa se pause por un tiempo especifico (usando la funcion sleep de la libreria ( time.sleep(tiempo en segundos) ))
import pycurl ## Libreria ( es necesario descargarla, no viene con python ), interfaz de python para libcurl http://pycurl.io/ , con esto se obtendra la informacion del archivo de texto proporcionado por xm.com.co
from io import BytesIO ## de la libreria io importar BytesIO, que permite leer y escribir objetos de tipo byte

## Funcion updateData, actualiza el archivo downData.txt con la informacion descargada en el tiempo de ejecucion
def updateData():

    now = datetime.date.today() ## Variable 'ahora', objeto, con la informacion sobre dia y hora

    day = '%02d' % now.day ## Variable day es igual al dia, si es menor de dos digitos se le agrega un cero
    month = '%02d' % now.month ## Variable month es igual al mes, si es menor de dos digitos se le agrega un cero
    year = now.year ## Variable year igual al año

    # Se genera el link, cada link tiene la misma estructura, solo cambian partes, con el año, mes y dia
    pagina = 'www.xm.com.co/despachonacional/' + str(year) + '-' + str(month) + '/dDEC' + str(month) + str(day) + '_NAL.TXT' ## Variable de tipo string, que genera un link basado en el dia actual

    ## Ejemplo sacado de la libreria pycurl ( https://github.com/pycurl/pycurl/blob/master/examples/quickstart/get_python3.py ) el resultado es parecido al ejecutar el programa cURL ( https://curl.haxx.se/ ) con el link generado 'string' (pedido HTTP GET)
    buffer = BytesIO() # BytesIO() devuelve el objeto buffer https://docs.python.org/3/library/io.html#buffered-streams
    c = pycurl.Curl() 
    c.setopt(c.URL, pagina)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    
    body = buffer.getvalue()

    global data
    data = body.decode('iso-8859-1').replace('\r', '') ## Ya que body es de tipo byte, hay que decodificarlo (Ej: Si se guarda directamente 'body', los caracteres \n y \r se guardaran como texto, y no como espacios), el codec en este caso es 'iso-8859-1' https://docs.python.org/3.6/library/codecs.html#standard-encodings, se remueven los caracteres return (\r) para eliminar espacios no necesarios del archivo
    if data.find('"page-not-found.aspx?404') == -1: ## Si se encuentra el string, significa que el archivo al que se intento acceder no existe, por lo cual sucede un error y el programa cierra
        file = open(path + "downData.txt", "w") # Abrir archivo de texto para escritura
        file.write(data) # Escribir la informacion en el archivo
