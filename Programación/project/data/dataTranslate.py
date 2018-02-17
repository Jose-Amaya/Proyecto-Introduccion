## revisar direccion
path = "/home/pi/project/data/files/" ## Informacion despacho nacional
path2 = "/home/pi/project/data/OfertaInicial (Alternativa)" ## Informacion no encontrada en despacho nacional

import sys # Para usar la funcion path.insert(), libreria para acceder a variables del interprete de python
sys.path.insert(0, path2) # Al importar la libreria, el interprete solo busca modulos en la direccion donde se encuentra el programa; dataTranslateO se encuentra en otra carpeta, para poder importarla se agrega la direccion al interprete
from dataTranslateO import updateCentrales # Importar la funcion updateCentrales de dataTranslateO (Informacion Guadalupe)

import time ## Libreria usada para hacer que el programa se pause por un tiempo especifico (usando la funcion sleep de la libreria ( time.sleep(tiempo en segundos) ))
import datetime # Libreria usada para obtener la hora
import ast ## Libreria usada para transformar el tipo de informacion que se obtiene del archivo de texto evaluandolo; este tipo es "string" o cadena; y se necesita una variable de tipo lista (o matriz) ( ast.literal_eval(string a evaluar) )

# declarar cs y eq como globales
global cs
global eq
## cs es la lista de centrales (con excepciones ( Se encuentra mas de una matriz de informacion, Ej: para Flores, se encuentra Flores1 y FloresIV ))
cs = ["E1","T1" ,"T1.1" ,"T1.4" ,"T2" ,"T3" ,"T3.11" ,"T3.21" ,"T4" ,"T4.1" ,"T4.2" ,"T5" ,"T6", "T7" ,"T7.1" ,"T7.2" ,"T7.3" ,"T7.4" ,"T8" ,"T9" ,"T9.2" ,"T9.3" ,"T9.4" ,"T9.5" ,"T10" ,"T10.1" ,"T10.2" ,"T10.3" , "T11" ,"H1" ,"H2" ,"H3" ,"H4" ,"H5" ,"H6" ,"H7" ,"H8" ,"H9" ,"H10" ,"H11" ,"H12" ,"H13" ,"H14" ,"H15" ,"H16" ,"H17" ,"H18" ,"H19" ,"H20" ,"H21" ,"H22" ,"H23" ,"H24" ,"H25" ,"H26" ,"H27" ,"H28" ,"H29" ,"H30" ,"H31" ,"H32" ,"H33" ,"H34" ,"H35"]
## eq es el diccionario de las equivalencias de las centrales con el nombre que aparece en XM en Despacho nacional, y el numero (Si tienen un punto, significa que la informacion hace parte de una misma central)
eq = {"E1": "MJEPIRAC" , "T1" : "None" ,"T1.1" : "FLORES1" ,"T1.4" : "FLORES IV" ,"T2" : "TEBSA" , "T3" : "None" ,"T3.11" : "GUAJIR11" ,"T3.21" : "GUAJIR21" , "T4" : "None" ,"T4.1" : "TASAJER1" ,"T4.2" : "TASAJERO2" ,"T5" : "TSIERRA" ,"T6" : "TEMCALI" , "T7" : "None" ,"T7.1" : "PAIPA1" ,"T7.2" : "PAIPA2" ,"T7.3" : "PAIPA3" ,"T7.4" : "PAIPA4" ,"T8" : "TCENTRO1" , "T9" : "None" ,"T9.2" : "ZIPAEMG2" ,"T9.3" : "ZIPAEMG3" ,"T9.4" : "ZIPAEMG4" ,"T9.5" : "ZIPAEMG5" , "T10" : "None" ,"T10.1" : "CTGEMG1" ,"T10.2" : "CTGEMG2" ,"T10.3" : "CTGEMG3" , "T11" : "MERILEC1" ,"H1" : "LAHERRADURA" ,"H2" : "JAGUAS" ,"H3" : "CSANCARLOS" ,"H4" : "SOGAMOSO" ,"H5" : "AMOYA" ,"H6" : "MIEL1" ,"H7" : "MCALDERAS" ,"H8" : "GUAVIO" ,"H9" : "BETANIA" ,"H10" : "ELQUIMBO" ,"H11" : "PAGUA PARAISO" ,"H12" : "PAGUA GUACA" ,"H13" : "MTEQUENDAMA" ,"H14" : "LATASAJERA" ,"H15" : "MCARACOLI" ,"H16" : "MLIMONAR" ,"H17" : "DARIOVS" ,"H18" : "MLAGUNETA" ,"H19" : "MPAJARITO" ,"H20" : "MSNJOSE_MONT" ,"H21" : "GUATRON" ,"H22" : "GUADALUPE3" ,"H23" : "GUADALUPE4" ,"H24" : "PORCE2" ,"H25" : "PORCE3" ,"H26" : "GUATAPE" ,"H27" : "MRIOABAJO" ,"H28" : "MSONSON" ,"H29" : "MRFRIOTAMES" ,"H30" : "M_AYURA" ,"H31" : "MNIQUIA" ,"H32" : "URRA" ,"H33" : "CHIVOR" ,"H34" : "CUCUANA" ,"H35" : "CALIMA1" }
## Lista de centrales (sin excepciones, nombres que aparecen en XM en Despacho nacional (# significa que hay varios datos y se sumaron))
loc = ['MJEPIRAC', 'FLORES#', 'TEBSA', 'GUAJIR#', 'TASAJER##', 'TSIERRA', 'TEMCALI', 'PAIPA#', 'TCENTRO1', 'ZIPAEMG#', 'CTGEMG#', 'MERILEC1', 'LAHERRADURA', 'JAGUAS', 'CSANCARLOS', 'SOGAMOSO', 'AMOYA', 'MIEL1', 'MCALDERAS', 'GUAVIO', 'BETANIA', 'ELQUIMBO', 'PAGUA PARAISO', 'PAGUA GUACA', 'MTEQUENDAMA', 'LATASAJERA', 'MCARACOLI', 'MLIMONAR', 'DARIOVS', 'MLAGUNETA', 'MPAJARITO', 'MSNJOSE_MONT', 'GUATRON', 'GUADALUPE3', 'GUADALUPE4', 'PORCE2', 'PORCE3', 'GUATAPE', 'MRIOABAJO', 'MSONSON', 'MRFRIOTAMES', 'M_AYURA', 'MNIQUIA', 'URRA', 'CHIVOR', 'CUCUANA', 'CALIMA1']
## Lista de centrales con nombres arbitrarios ( Nombres genericos, se usara para crear un diccionario ) 
genName = [ "JEPIRACHI1-15" , "FLORES" , "BARRANQUILLA" , "GUAJIRA" , "TASAJERO" , "TERMOSIERRAB" , "TERMOEMCALI1" , "PAIPA" , "TERMOCENTROCC" , "ZIPAEMG" , "CARTAGENA" , "MERILECTRICA1" , "LAHERRADURA" , "JAGUAS" , "SANCARLOS" , "SOGAMOSO" , "AMOYALAESPERANZA" , "MIELI" , "CALDERAS" , "GUAVIO" , "BETANIA" , "ELQUIMBO" , "PARAISO" , "LAGUACA", "TEQUENDAMA" , "LATASAJERA" , "CARACOLI" , "ELLIMONAR" , "DARIOVALENCIASAMPER" , "LAGUNETA" , "PAJARITO" , "SANJOSEDELAMONTAÑA" , "TRONERAS" , "GUADALUPE3" , "GUADALUPE4" , "PORCEII" , "PORCEIII" , "GUATAPE" , "RIOABAJO" , "SONSON" , "RIOFRIO(TAMESIS)" , "AYURA" , "NIQUIA" , "URRA1" , "CHIVOR" , "CUCUANA" , "CALIMA" ]


## en el diccionario Centrales se guardara toda la informacion
global Centrales
Centrales = {}

def matAdd(*args): ## Funcion para sumar matrices ( para las excepciones , toma un valor variable de argumentos, cada argumento debe ser una matriz del mismo tamaño)
    list = [args[x] for x in range(0,len(args))] # Se crea una lista de matrices (los argumentos)
    zipped_list = zip(*list) # Crear objeto de tipo zip con los elementos de la lista, Ej: para dos matrices, [1,2,3] y [4,5,6], los items seran (1,3), (2,5) y (3,6)
    result = [sum(item) for item in zipped_list] # Realizar la suma para los elementos de cada item Ej: item = (1,3), resultado: 4
    return result # Devolver el resultado

def matrixMake(Central): ## Funcion que devolvera una matriz con los valores de generacion para cada central

    file = open(path + "downData.txt") ## Se abre el archivo downData.txt donde esta la informacion para el dia de hoy
    data = file.read() ## Se lee y se guarda en 'data'

    if len(data) is not 0: ## Si el archivo downData.txt no esta abierto para escritura por otro programa ->

        file = open(path + "downData.txt") ## Abrir denuevo el archivo para lectura (al ejecutar el metodo .read() el archivo se cierra)
        matrix = [] ## Se define una matriz vacia donde se guardaran los valores, esta matriz sera devuelta por la funcion
        matrixString = "" ## Se define una cadena de caracteres, vacia, donde se guardara la informacion de la central

        global cs,eq ## Se toman la lista y el diccionario como globales

        if Central == "GUADALUPE3" or Central == "GUADALUPE4": # Excepcion, la informacion de GUADALUPE se obtiene de Oferta Inicial

            matrix = updateCentrales()[Central] # Ejecutar updateCentrales de dataTranslateO.py, y tomar la matriz de para la 'central'

        else:
            for x in file: ## para cada inea de data.txt
                if x.find(Central, 1, len(Central)+1) is not -1: ## Si se encuenta el nombre de una central en la linea ( string.find(String a buscar, inicio, final) ) el inicio es 1 ya que al inicio de cada linea se encuentra una doble comilla ( " )
                    matrixString = "[" + matrixString + x[len(Central)+3:len(x)].replace("\n", "") + "]" ## Guardar la informacion de la manera de una matriz y remover los caracteres newline (el tipo de informacion es string, pero tiene la forma de una matriz o lista, es decir Ej: [2,3,5] es una matriz, y "[2,3,5]" es un string, pero que puede ser evaluado para obtener una matriz)
                    matrix = ast.literal_eval(matrixString) ## Evaluar literalmente matrixString, devolviendo una matriz

        return matrix ## Devolver la matriz

def translateData(): ## Funcion "traducir informacion" actualiza el diccionario Centrales, y lo devuelve, cada central con sus datos para 24 horas
    for x in cs: ## para cada elemento de cs, es decir, cada central
    
        if ( eq[x] is not "None" ) and ( "." not in x ) and ( eq[x].find("PAGUA") is -1 ): ## Si el nombre de XM no es "None" (Excepciones) y ademas la key no tiene un punto (si tiene punto es una excepcion), Pagua es una excepcion porque dos centrales toman informacion de la matriz Pagua

            Centrales.update({eq[x]:matrixMake(eq[x])}) ## Actualizar el diccionario Centrales, agregando el nombre de la central, y su matriz

       ## Excepciones, centrales para las cuales hay mas de una matriz, sumar las matrices y despues agregar el nombre de excel al diccionario con la matriz resultante
    
        elif eq[x].find("PAGUA") is not -1: ## Si en el nombre de la central se encuentra Pagua

            if eq[x] == "PAGUA PARAISO": # Si es Pagua Paraiso
                Centrales.update({eq[x]:matrixMake("PAGUA")}) # ingresar Pagua Paraiso al diccionario con el valor de Pagua
            else: # Si no ( Pagua Guaca )
                Centrales.update({eq[x]:matrixMake("PAGUA")}) # ingresar Pagua Guaca al diccionario con el valor de Pagua

        # Para las excepciones (centrales con varias matrices) se toman las diferentes matrices que tienen, y despues se suman ( El procedimiento es el mismo para todas, solo se explica la primera excepcion )

        elif x == "T1": ## T1 Flores (Excepcion)

            mat1 = matrixMake(eq["T1.1"]) ## matriz 1 = primera matriz
            mat2 = matrixMake(eq["T1.4"]) ## matriz 2 = segunda matriz

            matr = matAdd(mat1,mat2) # matr = suma de las matrices

            Centrales.update({"FLORES#": matr}) # Agregar al diccionario la suma de las matrices

        elif x == "T3": ## T3 Guajira (Excepcion)

            mat1 = matrixMake(eq["T3.11"])
            mat2 = matrixMake(eq["T3.21"])

            matr = matAdd(mat1,mat2)

            Centrales.update({"GUAJIR#": matr})

        elif x == "T4": ## T4 Tasajero (Excepcion)

            mat1 = matrixMake(eq["T4.1"])
            mat2 = matrixMake(eq["T4.2"])

            matr = matAdd(mat1,mat2)

            Centrales.update({"TASAJER##": matr})

        elif x == "T7": ## T7 Paipa (Excepcion)

            mat1 = matrixMake(eq["T7.1"])
            mat2 = matrixMake(eq["T7.2"])
            mat3 = matrixMake(eq["T7.3"])
            mat4 = matrixMake(eq["T7.4"])

            matr = matAdd(mat1,mat2,mat3,mat4)

            Centrales.update({"PAIPA#": matr})

        elif x == "T9": ## T9 Zipa (San Martin) (Excepcion)

            mat1 = matrixMake(eq["T9.2"])
            mat2 = matrixMake(eq["T9.3"])
            mat3 = matrixMake(eq["T9.4"])
            mat4 = matrixMake(eq["T9.5"])

            matr = matAdd(mat1,mat2,mat3,mat4)

            Centrales.update({"ZIPAEMG#": matr})

        elif x == "T10": ## T10 CT Cartagena (Excepcion)

            mat1 = matrixMake(eq["T10.1"])
            mat2 = matrixMake(eq["T10.2"])
            mat3 = matrixMake(eq["T10.3"])

            matr = matAdd(mat1,mat2,mat3)

            Centrales.update({"CTGEMG#": matr})

    return Centrales

def translateDataGen(): ## Funcion "traducir informacion" pero con nombres generales (arbitrarios) ( Es decir cambiarle el nombre a las claves/llaves del diccionario )
    Centrales = translateData() # Actualizar el diccionario centrales
    for x in range(0,len(loc)): # para un rango de valores entre 0 y la cantidad de centrales
        Centrales.update({genName[x] : Centrales.pop(loc[x])}) ## Tomar el valor de la clave anterior para la central loc[x] ( Se elimina del diccionario ) y crear una nueva clave/llave tomando el nombre generico, y como valor, el valor tomado por la clave anterior
    return Centrales # Devolver el diccionario centrales

def uhour(): ## Esta funcion va a devolver una matriz con los datos de generacion de una planta para la respectiva hora (en 8 listas de 8 componentes)
    translateData() ## Actualizar el diccionario Centrales
    hr = datetime.datetime.today().hour ## Hora del dia
    matrix = [[0]*8 for x in range(0,8)] ## Matriz que va a ser devuelta, se crea con 8 listas de 8 componentes donde todos son 0
    for x in range(0,8): # Para x en un rango de 0 a 8 ( Se ejecuta 8 veces )
        for y in range(0,8): # Para y en un rango de 0 a 8 ( Se ejecuta 8 veces )
            place = y + x*8 # expresion place, para saber el numero del elemento que se esta evaluando ( Ej: para el ultimo valor de la matriz 8*8 devuelve 64 )
            if place < len(loc): # Si el numero del componente esta en el rango ( No se llenara toda la matriz, solo se tienen 47 valores )
                matrix[x][y] = Centrales[loc[place]][hr] ## Tomar la hora, y tomar el valor de la matriz dada por el diccionario para la central loc[place]
            else:
                matrix[x][y] = 0 ## Si no hay valores, el componente es 0
    return (matrix) # Devolver la matriz

def uhourCents(): ## Esta funcion va a devolver una lista con los datos de generacion de una planta para la respectiva hora
    translateData() ## Actualizar el diccionario Centrales
    hr = datetime.datetime.today().hour ## Hora del dia
    matrix = [0]*len(loc) ## Matrix que va a ser usada por infoWeb.py
    for x in range(0,len(loc)):
        matrix[x] = Centrales[loc[x]][hr] # Tomar el elemento 'hr' de la matriz 'loc[x]' siendo x el numero de la central, 'loc[x]' la central, y 'hr' la hora; Centrales[loc[x]] devuelve la matriz de valores de generacion en el dia para 'loc[x]'
    return (matrix) # Devolver la matriz

def actualMat(): ## Funcion que devuelve la informacion para poner en el archivo de texto que lee matS.py
    matrix = uhour() ## ejecutar funcion uHour, actualMat() solo convertira todo x > 0 en 1, y todo x = 0 se dejara igual, asi se tiene una matriz de unos y ceros, en vez de una matriz con varios valores positivos
    matS = [[0]*8 for x in range(0,8)] ## Matriz con 8 listas de 8 componentes que son ceros
    for x in range(0,8):
        for y in range(0,8):
            if matrix[x][y] == 0: ## Si para un elemento de la matriz devuelta por uhour, el valor es = 0
                matS[x][y] = 0 # El elemento de la nueva matriz es 0
            else: # Si no
                matS[x][y] = 1 # Es 1
    return(matS) # Devolver matriz

def actualMata(): ## Funcion que escribe la informacion dada por actualMat en el archivo que lee matS.py
    file2 = open(path + "matSdata.txt", "w") # Abrir archivo para escritura
    file2.write(str(actualMat())) # Escribir informacion
