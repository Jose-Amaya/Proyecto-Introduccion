## CHECK PATH
path = "./files/" ## For windows (VS)
## path = "/home/pi/project/data/OfertaInicial(Alternativa)/files/" ## For raspberry

import datetime
import time
import pycurl
from io import BytesIO

def updateData():

    now = datetime.date.today()

    day = '%02d' % now.day ## Variable day es igual al dia, si es menor de dos digitos se le agrega un cero
    month = '%02d' % now.month ## variable month es igual al mes, si es menor de dos digitos se le agrega un cero
    year = now.year ## variable year

    pagina = "http://www.xm.com.co/ofertainicial/" + str(year) + "-" + str(month) + "/OFEI" + str(month) + str(day) +".txt"

    ## Ejemplo sacado de la libreria
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, pagina)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    
    body = buffer.getvalue()
    # Body is a byte string.
    # We have to know the encoding in order to print it to a text file
    # such as standard output.
    ## print(body.decode('iso-8859-1'))

    global data
    data = body.decode('utf-8').replace("\r", '')
    if data.find('"page-not-found.aspx?404') == -1:
        file = open(path + "downDataO.txt", "w")
        file.write(data)