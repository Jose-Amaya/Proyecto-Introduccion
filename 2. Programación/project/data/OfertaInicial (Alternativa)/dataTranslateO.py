## CHECK PATH
path = "C:/Users/MEGA/Documents/GitHub/Proyecto-Introduccion/project/data/OfertaInicial (Alternativa)/files/" ## For windows (VS)
## path = "/home/pi/project/data/OfertaInicial (Alternativa)/files/" ## For raspberry

import time # Para esperar un tiempo especifico
import datetime # Para saber la hora
import ast # Para transformar la lista de numeros en una matriz

global cs
global eq
## cs es la lista de centrales
cs = [ "JEPIRACHI1-15" , "FLORES1" , "FLORES4B" , "BARRANQUILLA3" , "BARRANQUILLA4" , "TEBSAB" , "GUAJIRA1" , "GUAJIRA2" , "TASAJERO1" , "TASAJERO2" , "TERMOSIERRAB" , "TERMOEMCALI1" , "PAIPA1" , "PAIPA2" , "PAIPA3" , "PAIPA4" , "TERMOCENTROCC" , "ZIPAEMG2" , "ZIPAEMG3" , "ZIPAEMG4" , "ZIPAEMG5" , "CARTAGENA1" , "CARTAGENA2" , "CARTAGENA3" , "MERILECTRICA1" , "LAHERRADURA1" , "LAHERRADURA2" , "JAGUAS1" , "JAGUAS2" , "SANCARLOS1" , "SANCARLOS2" , "SANCARLOS3" , "SANCARLOS4" , "SANCARLOS5" , "SANCARLOS6" , "SANCARLOS7" , "SANCARLOS8" , "SOGAMOSO1" , "SOGAMOSO2" , "SOGAMOSO3" , "AMOYALAESPERANZA1" , "AMOYALAESPERANZA2" , "MIELI1" , "MIELI2" , "MIELI3" , "CALDERAS1" , "CALDERAS2" , "GUAVIO1" , "GUAVIO2" , "GUAVIO3" , "GUAVIO4" , "GUAVIO5" , "BETANIA1" , "BETANIA2" , "BETANIA3" , "ELQUIMBO1" , "ELQUIMBO2" , "PARAISO1" , "PARAISO2" , "PARAISO3" , "LAGUACA1" , "LAGUACA2" , "LAGUACA3" , "TEQUENDAMA" , "LATASAJERA1" , "LATASAJERA2" , "LATASAJERA3" , "CARACOLI" , "ELLIMONAR" , "DARIOVALENCIASAMPER1" , "DARIOVALENCIASAMPER2" , "DARIOVALENCIASAMPER5" , "LAGUNETA" , "PAJARITO" , "SANJOSEDELAMONTAÑA" , "TRONERAS1" , "TRONERAS2" , "GUADALUPE31" , "GUADALUPE32" , "GUADALUPE33" , "GUADALUPE34" , "GUADALUPE35" , "GUADALUPE36" , "GUADALUPE41" , "GUADALUPE42" , "GUADALUPE43" , "PORCEII1" , "PORCEII2" , "PORCEII3" , "PORCEIII4" , "PORCEIII3" , "PORCEIII2" , "PORCEIII1" , "GUATAPE1" , "GUATAPE2" , "GUATAPE3" , "GUATAPE4" , "GUATAPE5" , "GUATAPE6" , "GUATAPE7" , "GUATAPE8" , "RIOABAJO" , "SONSON" , "RIOFRIO(TAMESIS)" , "AYURA" , "NIQUIA" , "URRA1" , "CHIVOR1" , "CHIVOR2" , "CHIVOR3" , "CHIVOR4" , "CHIVOR5" , "CHIVOR6" , "CHIVOR7" , "CHIVOR8" , "CUCUANA1" , "CUCUANA2" , "CALIMA1" , "CALIMA2" , "CALIMA3" , "CALIMA4" ]
## Lista de centrales (Nombres arbitrarios)
genName = [ "JEPIRACHI1-15" , "FLORES" , "BARRANQUILLA" , "GUAJIRA" , "TASAJERO" , "TERMOSIERRAB" , "TERMOEMCALI1" , "PAIPA" , "TERMOCENTROCC" , "ZIPAEMG" , "CARTAGENA" , "MERILECTRICA1" , "LAHERRADURA" , "JAGUAS" , "SANCARLOS" , "SOGAMOSO" , "AMOYALAESPERANZA" , "MIELI" , "CALDERAS" , "GUAVIO" , "BETANIA" , "ELQUIMBO" , "PARAISO" , "LAGUACA", "TEQUENDAMA" , "LATASAJERA" , "CARACOLI" , "ELLIMONAR" , "DARIOVALENCIASAMPER" , "LAGUNETA" , "PAJARITO" , "SANJOSEDELAMONTAÑA" , "TRONERAS" , "GUADALUPE3" , "GUADALUPE4" , "PORCEII" , "PORCEIII" , "GUATAPE" , "RIOABAJO" , "SONSON" , "RIOFRIO(TAMESIS)" , "AYURA" , "NIQUIA" , "URRA1" , "CHIVOR" , "CUCUANA" , "CALIMA" ]
## Variable que define el tipo de informacion que se adquiere
info = " , D,  "

## Diccionario con centrales que tienen multiples datos
multDataDict = {"FLORES" : ["FLORES1" , "FLORES4B"] , "BARRANQUILLA" : ["BARRANQUILLA3" , "BARRANQUILLA4" , "TEBSAB"] , "GUAJIRA" : ["GUAJIRA1" , "GUAJIRA2"] , "TASAJERO" : ["TASAJERO1" , "TASAJERO2"] , "PAIPA" : ["PAIPA1" , "PAIPA2" , "PAIPA3" , "PAIPA4"] , "ZIPAEMG" : ["ZIPAEMG2" , "ZIPAEMG3" , "ZIPAEMG4" , "ZIPAEMG5"] , "CARTAGENA" : ["CARTAGENA1" , "CARTAGENA2" , "CARTAGENA3"] , "LAHERRADURA" : ["LAHERRADURA1" , "LAHERRADURA2"] , "JAGUAS" : ["JAGUAS1" , "JAGUAS2"] , "SANCARLOS" : ["SANCARLOS1" , "SANCARLOS2" , "SANCARLOS3" , "SANCARLOS4" , "SANCARLOS5" , "SANCARLOS6" , "SANCARLOS7" , "SANCARLOS8"] , "SOGAMOSO" : ["SOGAMOSO1" , "SOGAMOSO2" , "SOGAMOSO3"] , "AMOYALAESPERANZA" : ["AMOYALAESPERANZA1" , "AMOYALAESPERANZA2"] , "MIELI" : ["MIELI1" , "MIELI2" , "MIELI3"] , "CALDERAS" : ["CALDERAS1" , "CALDERAS2"] , "GUAVIO" : ["GUAVIO1" , "GUAVIO2" , "GUAVIO3" , "GUAVIO4" , "GUAVIO5"] , "BETANIA" : ["BETANIA1" , "BETANIA2" , "BETANIA3"] , "ELQUIMBO" : ["ELQUIMBO1" , "ELQUIMBO2"] , "PARAISO" : ["PARAISO1" , "PARAISO2" , "PARAISO3"] , "LAGUACA" : ["LAGUACA1" , "LAGUACA2" , "LAGUACA3"] , "LATASAJERA" : ["LATASAJERA1" , "LATASAJERA2" , "LATASAJERA3"] , "DARIOVALENCIASAMPER" : ["DARIOVALENCIASAMPER1" , "DARIOVALENCIASAMPER2" , "DARIOVALENCIASAMPER5"] , "TRONERAS" : ["TRONERAS1" , "TRONERAS2"] , "GUADALUPE3" : ["GUADALUPE31" , "GUADALUPE32" , "GUADALUPE33" , "GUADALUPE34" , "GUADALUPE35" , "GUADALUPE36"] , "GUADALUPE4" : ["GUADALUPE41" , "GUADALUPE42" , "GUADALUPE43"] , "PORCEII" : ["PORCEII1" , "PORCEII2" , "PORCEII3"] , "PORCEIII" : ["PORCEIII4" , "PORCEIII3" , "PORCEIII2" , "PORCEIII1"] , "GUATAPE" : ["GUATAPE1" , "GUATAPE2" , "GUATAPE3" , "GUATAPE4" , "GUATAPE5" , "GUATAPE6" , "GUATAPE7" , "GUATAPE8"] , "CHIVOR" : ["CHIVOR1" , "CHIVOR2" , "CHIVOR3" , "CHIVOR4" , "CHIVOR5" , "CHIVOR6" , "CHIVOR7" , "CHIVOR8"] , "CUCUANA" : ["CUCUANA1" , "CUCUANA2"] , "CALIMA" : ["CALIMA1" , "CALIMA2" , "CALIMA3" , "CALIMA4"]}
## lista de centrales con multiples datos
multDataList = ["FLORES" , "BARRANQUILLA" , "GUAJIRA" , "TASAJERO" , "PAIPA" , "ZIPAEMG" , "CARTAGENA" , "LAHERRADURA" , "JAGUAS" , "SANCARLOS" , "SOGAMOSO" , "AMOYALAESPERANZA" , "MIELI" , "CALDERAS" , "GUAVIO" , "BETANIA" , "ELQUIMBO" , "PARAISO" , "LAGUACA" , "LATASAJERA" , "DARIOVALENCIASAMPER" , "TRONERAS" , "GUADALUPE3" , "GUADALUPE4" , "PORCEII" , "PORCEIII" , "GUATAPE" , "CHIVOR" , "CUCUANA" , "CALIMA"]


## en el diccionario Centrales se guardara toda la informacion (con nombres arbitrarios), en CentralesN se guardaran con el numero
global Centrales,CentralesN
CentralesN = {}
Centrales = {}

## matriz para el programa matS.py
matSmat = [[0]*8 for x in range(0,8)]

def matAdd(*args): ## Funcion para sumar matrices
    list = [args[x] for x in range(0,len(args))] ## una lista con los argumentos que se le apliquen a la funcion, en este caso, una lista de las matrices a sumar
    zipped_list = zip(*list) ## Transponer las matrices, para despues poderlas sumar
    result = [sum(item) for item in zipped_list]
    return result

def matrixMake(Central): ## Funcion que devolvera una matriz con los valores de generacion para cada central

    file = open(path + "downDataO.txt") ## Se abre el archivo downDataO.txt donde esta la informacion para el dia de hoy
    data = file.read() ## Se lee

    if len(data) is not 0: ## Si el archivo downData.txt no ha sido abierto por otro programa...
        file = open(path + "downDataO.txt") ## Abrir el archivo (al ejecutar el metodo .read() el archivo se cierra)
        matrix = [] ## Se define una matriz vacia donde se guardaran los valores
        matrixString = "" ## Se define una cadena de caracteres, vacia, donde se guardara la informacion de la central

        global cs,eq,info ## Se toman las listas, y la variable info como globales

        for x in file: ## para cada linea de data.txt
            if x.find(Central + info, 0, len(Central + info)+1) is not -1: ## Si se encuentra el nombre de una central en la linea...
                matrixString = "[" + matrixString + x[len(Central + info):len(x)].replace("\n", "") + "]" ## Guardar la informacion de la manera de una matriz y remover los caracteres newline
                matrix = ast.literal_eval(matrixString) ## Evaluar literalmente matrixString, devolviendo una matriz

        return matrix ## Devolver la matriz

def translateData(): ## Funcion "traducir informacion" actualiza el diccionario Centrales, y lo devuelve, cada central con sus datos para 24 horas
    for x in cs: ## para cada elemento de cs, es decir, cada central
        CentralesN.update({x : matrixMake(x)}) ## Actualizar el diccionario Centrales, agregando el nombre de la central, y su matriz

    return CentralesN

def updateCentrales(): ## Funcion que actualizara el diccionario centrales, sumando la informacion de las diferentes matrices para las centrales que tienen mas de 1
    Centrales = translateData()
    for x in multDataList:
        Centrales.update({ x : matAdd( *[Centrales.pop(multDataDict[x][i]) for i in range(0,len(multDataDict[x]))] ) }) ## sumar las matrices de x central, retirarlas del diccionario, y agregar la suma con el nombre general
    return Centrales

def uhour(): ## Esta funcion va a devolver una matriz con los datos de generacion de una planta para la respectiva hora
    Centrales = updateCentrales() ## Actualizar el diccionario Centrales
    hr = datetime.datetime.today().hour ## Hora del dia
    matrix = [[0]*8 for x in range(0,8)] ## Matriz que va a ser actualizada y guardada en el archivo que lee matS.py
    for x in range(0,8):
        for y in range(0,8):
            if (y + x*8) < len(Centrales):
                matrix[x][y] = Centrales[genName[y + x*8]][hr]
            else:
                matrix[x][y] = 0
    return (matrix)

def uhourCents(): ## Esta funcion va a devolver una lista con los datos de generacion de una planta para la respectiva hora
    Centrales = updateCentrales() ## Actualizar el diccionario Centrales
    hr = datetime.datetime.today().hour ## Hora del dia
    matrix = [0]*len(genName) ## Matrix que va a ser usada por infoWeb.py
    for x in range(0,len(genName)):
        matrix[x] = Centrales[genName[x]][hr]
    return (matrix)

def actualMat(): ## Funcion que devuelve la informacion para poner en el archivo de texto que lee matS.py
    matrix = uhour()
    matS = [[0]*8 for x in range(0,8)]
    for x in range(0,8):
        for y in range(0,8):
            if matrix[x][y] == 0:
                matS[x][y] = 0
            else:
                matS[x][y] = 1
    return(matS)

def actualMata(): ## Funcion que escribe la informacipn dada por actualMat en el archivo que lee matS.py
    file2 = open(path + "matSdataO.txt", "w")
    file2.write(str(actualMat()))
