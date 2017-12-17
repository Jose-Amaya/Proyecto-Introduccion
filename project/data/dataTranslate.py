## CHECK PATH
path = "./files/" ## For windows (VS)
path2 = 'C:/Users/MEGA/Documents/GitHub/Proyecto-Introduccion/project/data/OfertaInicial (Alternativa)' ## Para Guadalupe
## path = "/home/pi/project/data/files/" ## For raspberry
## path 2 = "/home/pi/project/data/OfertaInicial (Alternativa)"

import sys
sys.path.insert(0, path2)
from dataTranslateO import updateCentrales

import time # Para esperar un tiempo especifico
import datetime # Para saber la hora
import ast # Para transformar la lista de numeros en una matriz

global cs
global eq
## cs es la lista de centrales (con excepciones)
cs = ["E1","T1" ,"T1.1" ,"T1.4" ,"T2" ,"T3" ,"T3.11" ,"T3.21" ,"T4" ,"T4.1" ,"T4.2" ,"T5" ,"T6", "T7" ,"T7.1" ,"T7.2" ,"T7.3" ,"T7.4" ,"T8" ,"T9" ,"T9.2" ,"T9.3" ,"T9.4" ,"T9.5" ,"T10" ,"T10.1" ,"T10.2" ,"T10.3" , "T11" ,"H1" ,"H2" ,"H3" ,"H4" ,"H5" ,"H6" ,"H7" ,"H8" ,"H9" ,"H10" ,"H11" ,"H12" ,"H13" ,"H14" ,"H15" ,"H16" ,"H17" ,"H18" ,"H19" ,"H20" ,"H21" ,"H22" ,"H23" ,"H24" ,"H25" ,"H26" ,"H27" ,"H28" ,"H29" ,"H30" ,"H31" ,"H32" ,"H33" ,"H34" ,"H35"]
## eq es el diccionario de centrales con el nombre que aparece en XM en Despacho nacional
eq = {"E1": "MJEPIRAC" , "T1" : "None" ,"T1.1" : "FLORES1" ,"T1.4" : "FLORES IV" ,"T2" : "TEBSA" , "T3" : "None" ,"T3.11" : "GUAJIR11" ,"T3.21" : "GUAJIR21" , "T4" : "None" ,"T4.1" : "TASAJER1" ,"T4.2" : "TASAJERO2" ,"T5" : "TSIERRA" ,"T6" : "TEMCALI" , "T7" : "None" ,"T7.1" : "PAIPA1" ,"T7.2" : "PAIPA2" ,"T7.3" : "PAIPA3" ,"T7.4" : "PAIPA4" ,"T8" : "TCENTRO1" , "T9" : "None" ,"T9.2" : "ZIPAEMG2" ,"T9.3" : "ZIPAEMG3" ,"T9.4" : "ZIPAEMG4" ,"T9.5" : "ZIPAEMG5" , "T10" : "None" ,"T10.1" : "CTGEMG1" ,"T10.2" : "CTGEMG2" ,"T10.3" : "CTGEMG3" , "T11" : "MERILEC1" ,"H1" : "LAHERRADURA" ,"H2" : "JAGUAS" ,"H3" : "CSANCARLOS" ,"H4" : "SOGAMOSO" ,"H5" : "AMOYA" ,"H6" : "MIEL1" ,"H7" : "MCALDERAS" ,"H8" : "GUAVIO" ,"H9" : "BETANIA" ,"H10" : "ELQUIMBO" ,"H11" : "PAGUA PARAISO" ,"H12" : "PAGUA GUACA" ,"H13" : "MTEQUENDAMA" ,"H14" : "LATASAJERA" ,"H15" : "MCARACOLI" ,"H16" : "MLIMONAR" ,"H17" : "DARIOVS" ,"H18" : "MLAGUNETA" ,"H19" : "MPAJARITO" ,"H20" : "MSNJOSE_MONT" ,"H21" : "GUATRON" ,"H22" : "GUADALUPE3" ,"H23" : "GUADALUPE4" ,"H24" : "PORCE2" ,"H25" : "PORCE3" ,"H26" : "GUATAPE" ,"H27" : "MRIOABAJO" ,"H28" : "MSONSON" ,"H29" : "MRFRIOTAMES" ,"H30" : "M_AYURA" ,"H31" : "MNIQUIA" ,"H32" : "URRA" ,"H33" : "CHIVOR" ,"H34" : "CUCUANA" ,"H35" : "CALIMA1" }
## Lista de centrales (sin excepciones, nombres que aparecen en XM en Despacho nacional (# significa que hay varios datos y se sumaron))
loc = ['MJEPIRAC', 'FLORES#', 'TEBSA', 'GUAJIR#', 'TASAJER##', 'TSIERRA', 'TEMCALI', 'PAIPA#', 'TCENTRO1', 'ZIPAEMG#', 'CTGEMG#', 'MERILEC1', 'LAHERRADURA', 'JAGUAS', 'CSANCARLOS', 'SOGAMOSO', 'AMOYA', 'MIEL1', 'MCALDERAS', 'GUAVIO', 'BETANIA', 'ELQUIMBO', 'PAGUA PARAISO', 'PAGUA GUACA', 'MTEQUENDAMA', 'LATASAJERA', 'MCARACOLI', 'MLIMONAR', 'DARIOVS', 'MLAGUNETA', 'MPAJARITO', 'MSNJOSE_MONT', 'GUATRON', 'GUADALUPE3', 'GUADALUPE4', 'PORCE2', 'PORCE3', 'GUATAPE', 'MRIOABAJO', 'MSONSON', 'MRFRIOTAMES', 'M_AYURA', 'MNIQUIA', 'URRA', 'CHIVOR', 'CUCUANA', 'CALIMA1']
## Lista de centrales con nombres arbitrarios
genName = [ "JEPIRACHI1-15" , "FLORES" , "BARRANQUILLA" , "GUAJIRA" , "TASAJERO" , "TERMOSIERRAB" , "TERMOEMCALI1" , "PAIPA" , "TERMOCENTROCC" , "ZIPAEMG" , "CARTAGENA" , "MERILECTRICA1" , "LAHERRADURA" , "JAGUAS" , "SANCARLOS" , "SOGAMOSO" , "AMOYALAESPERANZA" , "MIELI" , "CALDERAS" , "GUAVIO" , "BETANIA" , "ELQUIMBO" , "PARAISO" , "LAGUACA", "TEQUENDAMA" , "LATASAJERA" , "CARACOLI" , "ELLIMONAR" , "DARIOVALENCIASAMPER" , "LAGUNETA" , "PAJARITO" , "SANJOSEDELAMONTAÑA" , "TRONERAS" , "GUADALUPE3" , "GUADALUPE4" , "PORCEII" , "PORCEIII" , "GUATAPE" , "RIOABAJO" , "SONSON" , "RIOFRIO(TAMESIS)" , "AYURA" , "NIQUIA" , "URRA1" , "CHIVOR" , "CUCUANA" , "CALIMA" ]


## en el diccionario Centrales se guardara toda la informacion
global Centrales
Centrales = {}

def matAdd(*args): ## Funcion para sumar matrices
    list = [args[x] for x in range(0,len(args))]
    zipped_list = zip(*list)
    result = [sum(item) for item in zipped_list]
    return result

def matrixMake(Central): ## Funcion que devolvera una matriz con los valores de generacion para cada central

    file = open(path + "downData.txt") ## Se abre el archivo downData.txt donde esta la informacion para el día de hoy
    data = file.read() ## Se lee

    if len(data) is not 0: ## Si el archivo downData.txt no ha sido abierto por otro programa...

        file = open(path + "downData.txt") ## Abrir el archivo (al ejecutar el metodo .read() el archivo se cierra)
        matrix = [] ## Se define una matriz vacia donde se guardaran los valores
        matrixString = "" ## Se define una cadena de caracteres, vacia, donde se guardara la informacion de la central

        global cs,eq ## Se toman la lista y el diccionario como globales

        if Central == "GUADALUPE3" or Central == "GUADALUPE4":

            matrix = updateCentrales()[Central]

        else:
            for x in file: ## para cada inea de data.txt
                if x.find(Central, 1, len(Central)+1) is not -1: ## Si se encuentra el nombre de una central en la linea...
                    matrixString = "[" + matrixString + x[len(Central)+3:len(x)].replace("\n", "") + "]" ## Guardar la informacion de la manera de una matriz y remover los caracteres newline (el tipo de informacion es string, pero tiene la forma de una matriz o lista)
                    matrix = ast.literal_eval(matrixString) ## Evaluar literalmente matrixString, devolviendo una matriz
        

        return matrix ## Devolver la matriz

def translateData(): ## Funcion "traducir informacion" actualiza el diccionario Centrales, y lo devuelve, cada central con sus datos para 24 horas
    for x in cs: ## para cada elemento de cs, es decir, cada central
    
        if ( eq[x] is not "None" ) and ( "." not in x ) and ( eq[x].find("PAGUA") is -1 ): ## Si el nombre de XM no es "None" (Excepciones) y ademas la key no tiene un punto (si tiene punto es una excepcion)

            Centrales.update({eq[x]:matrixMake(eq[x])}) ## Actualizar el diccionario Centrales, agregando el nombre de la central, y su matriz

       ## Excepciones, centrales para las cuales hay mas de una matriz, sumar las matrices y despues agregar el nombre de excel al diccionario con la matriz resultante
    
        elif eq[x].find("PAGUA") is not -1:

            if eq[x] == "PAGUA PARAISO":
                Centrales.update({eq[x]:matrixMake("PAGUA")})
            else:
                Centrales.update({eq[x]:matrixMake("PAGUA")})

        elif x == "T1": ## T1 Flores

            mat1 = matrixMake(eq["T1.1"])
            mat2 = matrixMake(eq["T1.4"])

            matr = matAdd(mat1,mat2)

            Centrales.update({"FLORES#": matr})

        elif x == "T3": ## T3 Guajira

            mat1 = matrixMake(eq["T3.11"])
            mat2 = matrixMake(eq["T3.21"])

            matr = matAdd(mat1,mat2)

            Centrales.update({"GUAJIR#": matr})

        elif x == "T4": ## T4 Tasajero

            mat1 = matrixMake(eq["T4.1"])
            mat2 = matrixMake(eq["T4.2"])

            matr = matAdd(mat1,mat2)

            Centrales.update({"TASAJER##": matr})

        elif x == "T7": ## T7 Paipa

            mat1 = matrixMake(eq["T7.1"])
            mat2 = matrixMake(eq["T7.2"])
            mat3 = matrixMake(eq["T7.3"])
            mat4 = matrixMake(eq["T7.4"])

            matr = matAdd(mat1,mat2,mat3,mat4)

            Centrales.update({"PAIPA#": matr})

        elif x == "T9": ## T9 Zipa (San Martin)

            mat1 = matrixMake(eq["T9.2"])
            mat2 = matrixMake(eq["T9.3"])
            mat3 = matrixMake(eq["T9.4"])
            mat4 = matrixMake(eq["T9.5"])

            matr = matAdd(mat1,mat2,mat3,mat4)

            Centrales.update({"ZIPAEMG#": matr})

        elif x == "T10": ## T10 CT Cartagena

            mat1 = matrixMake(eq["T10.1"])
            mat2 = matrixMake(eq["T10.2"])
            mat3 = matrixMake(eq["T10.3"])

            matr = matAdd(mat1,mat2,mat3)

            Centrales.update({"CTGEMG#": matr})

    return Centrales

def translateDataGen(): ## Funcion "traducir informacion" pero con nombres generales (arbitrarios)
    Centrales=translateData()
    for x in range(0,len(loc)):
        Centrales.update({genName[x] : Centrales.pop(loc[x])})
    return Centrales

def uhour(): ## Esta funcion va a devolver una matriz con los datos de generacion de una planta para la respectiva hora (en 8 listas de 8 componentes)
    translateData() ## Actualizar el diccionario Centrales
    hr = datetime.datetime.today().hour ## Hora del dia
    matrix = [[0]*8 for x in range(0,8)] ## Matriz que va a ser actualizada y guardada en el archivo que lee matS.py
    for x in range(0,8):
        for y in range(0,8):
            place = y + x*8
            if place < len(loc):
                matrix[x][y] = Centrales[loc[place]][hr]
            else:
                matrix[x][y] = 0
    return (matrix)

def uhourCents(): ## Esta funcion va a devolver una lista con los datos de generacion de una planta para la respectiva hora
    translateData() ## Actualizar el diccionario Centrales
    hr = datetime.datetime.today().hour ## Hora del dia
    matrix = [0]*len(loc) ## Matrix que va a ser usada por infoWeb.py
    for x in range(0,len(loc)):
        matrix[x] = Centrales[loc[x]][hr]
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

def actualMata(): ## Funcion que escribe la informacion dada por actualMat en el archivo que lee matS.py
    file2 = open(path + "matSdata.txt", "w")
    file2.write(str(actualMat()))