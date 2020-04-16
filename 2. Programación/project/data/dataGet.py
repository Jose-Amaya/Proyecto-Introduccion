import os

saveData = True

deployed = os.name == 'posix'

if deployed:
    path = "/home/pi/project/data/files/"
else:
    path = os.getcwd() + "\\2. Programación\\project\\data\\files\\"

import datetime # Libreria usada para obtener dia y hora
import urllib.request as req

# Perform http request and return the response
def performRequest(page, requestUri, textEncoding):
    if not deployed:
        print(page + requestUri)
    
    try:
        response = req.urlopen("http://" + page + requestUri)
    except:
        return("ERROR DATAGET: Can't open URL")

    status = response.status

    if status != 200: # If the status is not 200 (OK)
        return("ERROR DATAGET: Status %d" % status)

    try:
        response = response.read()
    except:
        return("ERROR DATAGET: Can't read response")

    if len(response) == 0:
        return("ERROR DATAGET: Response length is 0")

    response = response.decode(encoding=textEncoding)

    return(response)


# Save the file checking for errors
def saveFile(data, filename, fileEncoding):
    file = open(path + filename, "w", encoding = fileEncoding, newline='') # Abrir archivo de texto para escritura
    file.write(data) # Escribir la informacion en el archivo
    file.close()

## getData function, returns downloaded data without parsing
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
