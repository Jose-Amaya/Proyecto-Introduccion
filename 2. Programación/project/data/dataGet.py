import os

saveData = True

deployed = os.name == 'posix'

if deployed:
    path = "/home/pi/project/data/files/"
else:
    path = os.getcwd() + "\\2. Programación\\project\\data\\files\\"

import datetime # Libreria usada para obtener dia y hora
import socket
import re
import json

# Perform http request and return the response
def performRequest(page, requestUri, textEncoding):
    if not deployed:
        print(page + requestUri)

    dataSocket = socket.socket()
    dataSocket.settimeout(1)
    try:
        dataSocket.connect((page,80))
    except:
        return("ERROR DATAGET: Can't connect to server (Check timeout)")

    dataSocket.send(b"GET %b HTTP/1.1\r\nHost: www.xm.com.co\r\n\r\n" % requestUri.encode(encoding="utf-8"))
    
    response = bytes()

    try:
        temp = dataSocket.recv(2048)
    except socket.timeout:
        return("ERROR DATAGET: Error first receive (timeout)")
    except:
        return("ERROR DATAGET: Error first receive (unknown)")
    response += temp

    while True:
        try:
            temp = dataSocket.recv(2048)
        except socket.timeout:
            break
        except:
            return("ERROR DATAGET: Error receiving (unknown)")

        response += temp

    dataSocket.shutdown(socket.SHUT_RDWR)
    dataSocket.close()

    response = response.decode(encoding=textEncoding)

    # Check if the file is complete
    contentLength = re.search('Content-Length: (\d+)', response)
    if contentLength:
        contentLength = int(contentLength.group(1))
    else:
        return("ERROR DATAGET: No Content-Length")

    headerEnd = re.search('\r\n\r\n', response)
    if headerEnd:
        actualLength = len(response[headerEnd.span()[1]:].encode(textEncoding))
    else:
        return("ERROR DATAGET: Cannot find Header")

    if actualLength != contentLength:
        return("ERROR DATAGET: Length does not match")

    if (response.find('"page-not-found.aspx?404') == -1) and (response.find('404 NOT FOUND') == -1): # If the page is not found
        return(response)
    else:
        return("ERROR DATAGET: 404 Not Found")

# Save the file checking for errors
def saveFile(data, filename, fileEncoding):
    file = open(path + filename, "w", encoding = fileEncoding, newline='') # Abrir archivo de texto para escritura
    file.write(data) # Escribir la informacion en el archivo
    file.close()

## Funcion updateData, actualiza el archivo downData.txt con la informacion descargada en el tiempo de ejecucion
def getData():

    now = datetime.date.today() ## Variable 'ahora', objeto, con la informacion sobre dia y hora

    day = '%02d' % now.day
    month = '%02d' % now.month
    year = str(now.year)

    pagina = "www.xm.com.co"
    requestUriDN = '/despachonacional/' + year + '-' + month + '/dDEC' + month + day + '_NAL.TXT' # URI para despacho nacional
    requestUriOI = '/ofertainicial/' + year + '-' + month + '/OFEI' + month + day + '.txt' # URI para oferta inicial 

    despachoNacional = performRequest(pagina, requestUriDN, "iso-8859-1")
    ofertaInicial = performRequest(pagina, requestUriOI, "utf-8")

    if saveData:
        saveFile(despachoNacional, "despachoNacional.txt", "iso-8859-1")
        saveFile(ofertaInicial, "ofertaInicial.txt", "utf-8")

    return([despachoNacional, ofertaInicial])