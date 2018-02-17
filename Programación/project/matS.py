## Este programa se corre junto a dataUpdater.py
## Revisar direccion path
path = "/home/pi/project/data/files/" ## direccion al archivo files, si la carpeta project se encuentra en /home/pi

# Importar librerias necesarias para el funcionamiento
import RPi.GPIO as GPIO ## Se importa la libreria RPi.GPIO, y se le da el nombre de GPIO para que sea de mas facil acceso (para llamar una funcion de la liberia se usara GPIO.funcion en vez de RPi.GPIO.funcion) esta libreria permite controlar la funcion y el estado de los pines de la raspbery
import time ## Libreria usada para hacer que el programa se pause por un tiempo especifico (usando la funcion sleep de la libreria ( time.sleep(tiempo en segundos) ))
import ast ## Libreria usada para transformar el tipo de informacion que se obtiene del archivo de texto evaluandolo; este tipo es "string" o cadena; y se necesita una variable de tipo lista (o matriz) ( ast.literal_eval(string a evaluar) )

GPIO.setmode(GPIO.BOARD) ## Hay varias maneras de numerar los pines de la raspberry, aca se define el tipo de numeracion que se va a usar

wt = 0.001 ## Una variable que representa el tiempo que una fila de leds va a estar prendida

global matrix ## Definicion de la variable global matrix, la cual tendra la informacion de que leds tienen que estar encendidos
matrix = [[0]*8 for x in range(0,8)] ## Se crea una matriz 8x8 de ceros (una lista, compuesta por 8 listas, compuestas cada una por 8 ceros)

column = [18, 22, 24, 26, 32, 36, 38, 40] # Lista de los pines que van conectados a la PCB, 'BP1' -> 'BP8' ('P1' -> 'P8' Esquema PCB 'tarjeta.brd')
row = [11, 7, 5, 3, 37, 35, 33, 31] # Lista de los pines que van conectados a la PCB, 'BN1' -> 'BN8' (Esquema PCB 'tarjeta.brd')

## Configurar los pines column y row como salidas
for i in row:
    GPIO.setup(i, GPIO.OUT) ## Para cada elemento de la lista row (es decir, el numero de un pin) configurarlo como salida
for x in column:
    GPIO.setup(x, GPIO.OUT) ## Para cada elemento de la lista column (es decir, el numero de un pin) configurarlo como salida

try: # Para manejo de errores, se trata de ejecutar esta parte del codigo, si sucede el evento descrito despues de 'except', se ejecuta otra parte del codigo, y al cerrar el programa manualmente, se ejecuta la parte de codigo despues de 'finally'

## Definicion de una funcion, llamada allofon ( todos apagados ) , que no toma argumentos, y cambia el estado de todos los pines en las listas row y column, como low/0/apagado (Apaga todos los leds)
    def allofon():
        for i in row: # Para cada elemento de la lista row (Pines de la raspberry, conectados a 'BP8' -> 'BP1')
            GPIO.output(i, False) # Definir el estado del pin como low/0/apagado
        for x in column: # Para cada elemento de la lista column (Pines de la raspberry, conectados a 'BN1' -> 'BN8')
            GPIO.output(x, False) # Definir el estado del pin como low/0/apagado

## Definicion de una funcion, llamada updateleds ( actualizar leds ), la cual actualiza el estado de los leds, la cual prende y apaga los leds de manera rapida, para esto, se miran los datos de cada fila, si se necesita encender un led en una fila, se enciende la fila y los leds, despues se esperan 'wt' segundos, se apagan todos los leds, y se continua con las siguientes filas
    def updateleds(): ## Configurar el estado de los pines

        for x in range(0,8): ## Ciclo for, que se ejecuta 8 veces ( range(0,8) es una lista de 8 elementos, los numeros de 0 a 7 ), este ciclo servira para acceder a cada fila de 'matrix' ( Cada fila de 'matrix' representa un pin conectado a un 'BN' de la PCB, esta lista contiene 8 elementos, cada uno, un uno o un cero, que corresponden al estado de cada pin 'P' en la fila respectiva )
                if 1 in matrix[x]: ## Si se necesita encender al menos un led en la lista numero x de 'matrix' ( Es decir si se encuentra un 1, ya que si para la fila x, no hay leds por encender, los elementos de la lista seran ceros ), encender el pin correspondiente a la fila x
                    GPIO.output(row[x], True) ## (Ej: Si la fila 1 ( matrix[0] ) contiene un 1, encender pin correspondiente a la fila 1 , es decir, BN1, que es el primer elemento de 'row' ( row[0] ))
                    for i in range(0,7): ## En la PCB, hay 7 columnas ( 'P8' ( column[7] ) no tiene leds conectados ), este ciclo for servira para acceder a cada valor de la lista 'matrix[x]' ( Ej: El elemento 2 de la fila 1 ( LED conectado con la Fila 'BN1', Columna 'P2' ) matrix[0][1] )
                        if matrix[x][i] == 1: ## Se miran cuales leds de la fila se necesitan encender
                            GPIO.output(column[i], True) ## Si se necesita encender un led en la columna i, encender el pin correspondiente a la columna ( estado high/1/encendido )
                    w() ## funcion para esperar 'wt' segundos ( definida despues )
                    allofon() ## Apagar todos los leds, para despues continuar con la siguiente fila

## Definicion de la funcion from88to87mat  ( de una matriz 8*8 a una matriz 8*7 ), que toma de argumentos una matrix 8*8 y devuelve una matriz 8*7 ( 8 filas, 7 columnas ) ( los ultimos elementos de 'matrix' se ignoran , ya que solo se muestra informacion sobre 47 centrales )
    def from88to87mat(mat):
        longMat = [] ## definicion de una matriz sin elementos
        for x in range(0,8): # Ciclo for que se ejecuta 8 veces, cada vez tomando un numero en orden de 0 -> 8
            for y in range(0,8): # Ciclo for que se ejecuta 8 veces, cada vez tomando un numero en orden de 0 -> 8
                longMat.append(mat[x][y]) # Agregar a la matriz longMat, el elemento mat[x][y] de la matriz ( Estos dos ciclos for, acceden a cada elemento de la matriz 'mat' ( que al ejecutar la funcion sera 'matrix' ) y lo añaden a la lista longMat )
                ## Al ejecutarse los ciclos for, la matriz 'longMat' es una lista de 64 elementos, con los datos de 'mat'

        the87mat = [] ## definicion de matriz sin elementos, esta sera la matriz que devuelva la funcion

        for x in range(0,8): # Ciclo for que se ejecuta 8 veces ( Una vez por cada fila )

            phmat = [] ## lista placeholder, para guardar datos temporalmente en el ciclo for, la 'fila' x de longMat ( un grupo de 7 elementos )

            for y in range(0,7): # Ciclo for que se ejecuta 7 veces ( Una vez por cada columna )
                phmat.append(longMat[y+x*7]) ## Tomar el elemento numero y + x*7 ( longMat tiene 64 elementos , si se mira como una matriz 7*8, cada grupo de 7 elementos es una fila, con la expresion y + x*7 se accederia al elemento 'y' de la fila 'x' )

            the87mat.append(phmat) ## Agregar la lista phmat a la matriz the87mat

        return the87mat ## devolver la matriz 8*7

## Definicion de la funcion updatedata ( actualizar informacion ), la cual no toma argumentos, esta funcion actualiza 'matrix' de acuerdo a la informacion en ./files/matSdata.txt ( archivo de texto )
    def updatedata():
        global matrix ## Tomar la variable global 'matrix', para no crear otra variable matrix dentro de la funcion
        file = open(path + "matSdata.txt","r") ## Abrir el archivo donde estaran los datos ( la variable path, definida al principio del programa, es la direccion al archivo ) para lectura ("r" (read))

        """
        #### Los datos se pueden conseguir de Oferta nacional, o de oferta inicial, quitar el comentario para tomar los datos de oferta inicial
        file = open ("/home/pi/project/data/OfertaInicial (Alternativa)/files/matSdataO.txt","r") ## abrir el archivo para lectura ("r" (read))
        """

        placeHolder = file.read() ## Una variable, llamada placeHolder, la cual sera de tipo string, con la informacion del archivo de texto
        if len(placeHolder) is not 0: ## Comprueba que la variable placeHolder tenga mas de 0 caracteres, esto sucede si al leer el archivo, este esta abierto para escritura por otro programa ( Puede pasar cuando se actualiza el archivo ), es decir, no se puede leer, y file.read() no devuelve nada

            matrix = from88to87mat(ast.literal_eval(placeHolder)) ## Se evalua literalmente el string placeHolder, esto devuelve una matriz ( Ej: ast.literal_Eval("[0,3,4]") devuelve la matriz [0,3,4] | Ej2: ast.literal_eval("2+2") devuelve 4 )

## Definicion de la funcion w ( wait ), Funcion que hace que el programa espere 'wt' segundos ( variable definida anteriormente ) antes de continuar ejecutandose
    def w():
        time.sleep(wt) ## Se hace uso de la funcion sleep de la libreria time, y se ingresa el valor de segundos, que en este caso es la variable 'wt'
       
    while True: ## Ciclo infinito, Parte del codigo que se ejecutara mientras el programa este corriendo
        updatedata() ## Se lee la informacion del archivo de texto, y se actualiza 'matrix' de acuerdo a lo que se lea
        updateleds() ## Actualizar los leds de acuerdo a la informacion de 'matrix'

except KeyboardInterrupt: ## si al ejecutarse el programa en una consola, se presiona CTRL + C
    allofon() ## Apagar la matriz
    GPIO.cleanup() ## Devolver los pines a su estado original para que puedan ser usados por otro programa ( Si no se ejecuta esta funcion, los pines definidos como salida, quedan definidos como salida )

finally: ## Al cerrar el programa de manera manual
    allofon() ## Apagar la matriz
    GPIO.cleanup() ## ## Devolver los pines a su estado original para que puedan ser usados por otro programa ( Si no se ejecuta esta funcion, los pines definidos como salida, quedan definidos como salida )