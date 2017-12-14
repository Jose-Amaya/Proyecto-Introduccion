## CHECK PATH

import RPi.GPIO as GPIO ## Se importan la libreria RPi.GPIO, y se le da el nombre de GPIO para que sea de mas facil acceso, para llamar una funcion de la liberia se usara GPIO.funcion en vez de RPi.GPIO.funcion, esta libreria permite controlar los pines de la raspbery
import time ## Libreria usada para hacer que el programa se pause por un tiempo especifico (usando la funcion sleep de la libreria)
import ast ## Libreria usada para transformar el tipo de informacion que se obtiene del archivo de texto, este tipo es "string" o cadena, porque es una cadena de caracteres, y se va a usar para transformar esa string a una lista

GPIO.setmode(GPIO.BOARD) ## Hay varias maneras de numerar los pines de la raspberry, aca se define el tipo de numeracion que se va a usar

wt = 0.001 ##Una variable que representa el tiempo que una fila de leds va a estar prendida


#### CODIGO PARA LA MATRIZ DE PRUEBA START
matrix = [[0]*8 for x in range(0,8)] ## Se crea una matriz, una lista, compuesta por 8 listas, compuestas cada una por 8 ceros

row = [3,5,7,11,13,15,19,21] ## Estos son los numeros de los pines que van a controlar el voltaje que llega a los anodos de los leds, son las filas, si su estado es positivo, se va a encender la fila
column = [8,10,12,16,18,22,24,26] ## Pines que van a controlar el voltaje que llega a los catodos de los leds, son las columnas, si su estado es negativo, se va a encender la columna
#### END

"""
#### Para la matrix real

row = [18, 22, 24, 26, 32, 36, 38, 40] # rojo en brd PCB P8 -> P1
column = [11, 7, 5, 3, 8, 7, 6, 5] # azul en brd PCB BN pins

"""

    ## Setup the outputs
for i in row:
    GPIO.setup(i, GPIO.OUT) ## Para cada elemento de la lista row, que es el numero de un pin, configurarlo como una salida
for x in column:
    GPIO.setup(x, GPIO.OUT) ## lo mismo pero para las columnas

try:
    #### CODIGO PARA LA MATRIZ DE PRUEBA START
    def allofon(): ## Se define una funcion, que va a apagar toda la matriz, para esto, van a poner todos los pines de las filas en estado negativo, y todos los pines de las columnas en estado positivo
        for i in row:
            GPIO.output(i, False)
        for x in column:
            GPIO.output(x, True)
    #### END

    """
    #### Para la matriz real

    def alloff(): ## Se define una funcion, que va a apagar toda la matriz
        for i in row:
            GPIO.output(i, False)
        for x in column:
            GPIO.output(x, False)

    """

    #### CODIGO PARA LA MATRIZ DE PRUEBA START
    def updateleds(): ## Configurar el estado de los pines (True = Positivo, False = Negativo) de acuerdo a los datos de la matriz (La primera fila, es representada por la primera lista de la matriz, el primer led en dicha fila, es el primer valor de dicha lista)
        
        for x in range(0,8):
                if 1 in matrix[x]: ## Si se necesita preder un led en la lista numero x, encender el pin correspondiente a la fila (Se configuran los leds para que su estado sea positivo)
                    GPIO.output(row[x], True)

                    for i in range(0,8):
                        if matrix[x][i] == 1: ## Se miran cuales leds de la fila se necesitan encender
                            GPIO.output(column[i], False) ## Se configura el estado de las columnas a negativo para encender los leds de estas columnas para la fila x
                    w() ## funcion, definida despues
                    allofon() ## Apagar todos los leds, para despues continuar con la siguiente fila
    #### END

    """
    #### Para la matriz real

    def updateleds(): ## Configurar el estado de los pines
        
        for x in range(0,8):
                if 1 in matrix[x]: ## Si se necesita prender un led en la lista numero x, encender el pin correspondiente a la fila
                    GPIO.output(row[x], True)

                    for i in range(0,7): ## 7 columnas
                        if matrix[x][i] == 1: ## Se miran cuales leds de la fila se necesitan encender
                            GPIO.output(column[i], True) ## Se configura el estado de las columnas a positivo para prender los leds correspondientes
                    w() ## funcion, definida despues
                    allofon() ## Apagar todos los leds, para despues continuar con la siguiente fila

    """
    """
    #### Para la matriz real
    def from88to87mat(mat): ## Transforma la matriz de entrada 8*8 a una matriz de 8*7 y se devuelve
        longMat = []
        for x in range(0,8):
            for y in range(0,8):
                longMat.append(mat[x][y])

        the87mat = []

        for x in range(0,8):

            phmat = []

            for y in range(0,7):
                phmat.append(longMat[y+x*7])

            the87mat.append(phmat)

        return the87mat
    """


    def updatedata(): ## Funcion definida para obtener la informacion del archivo de texto
        global matrix ## Tomar la variable global "matrix", esto evita que se cree una nueva variable dentro de la funcion
        file = open("/home/pi/project/data/files/matSdata.txt","r") ## Abrir el archivo donde estaran los datos

        """
        #### para datos de OfertaInicial:
        file = open ("/home/pi/project/data/OfertaInicial (Alternativa)/files/matSdata.txt","r")

        """
        placeHolder = file.read() ## Una variable, llamada placeHolder, sera igual a los datos que tenga el archivo de texto
        if len(placeHolder) is not 0: ## Comprueba que la variable placeHolder tenga mas de 0 caracteres, esto sucede si al leer el archivo, este esta abierto por otro programa, por lo que la variable placeHolder no tendra informacion
            #### CODIGO PARA LA MATRIZ DE PRUEBA START
            matrix = ast.literal_eval(placeHolder) ## matrix sera igual a la evaluacion literal de la variable placeHolder, la variable placeHolder es de tipo string, esto convierte esta variable en una matriz
            #### END
            """
            #### Para la matriz real
            matrix = from88to87mat(ast.literal_eval(placeHolder))
            """
    
    def w(): ## Funcion que hace que el programa espere "wt" (variable definida anteriormente) segundos antes de continuar ejecutandose
        time.sleep(wt) ## Se hace uso de la funcion sleep de la libreria time, y se ingresa el valor de segundos, que en este caso es la variable wt
       
    while True: ## Ciclo infinito, el codigo de abajo se ejecutara mientras el programa este abierto
        updatedata() ## Se lee la informacion del archivo de texto, y se actualiza matrix de acuerdo a lo que se lea
        updateleds() ## Actualizar los leds de acuerdo a la informacion de matrix

except KeyboardInterrupt:
    allofon() ## Apagar la matriz
    GPIO.cleanup() ## Devolver los pines a su estado original para que puedan ser usados por otro programa

finally: ## Al cerrar el programa de manera manual
    allofon() ## Apagar la matriz
    GPIO.cleanup() ## Devolver los pines a su estado original para que puedan ser usados por otro programa
