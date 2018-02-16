# Proyecto-Introduccion

Los archivos principales se encuentran en la carpeta "project"

Se planean utilizar los datos de Despacho Nacional, pero si es necesario, se pueden utilizar los datos de Oferta inicial, para esto se ejecuta dataUpdaterO.py (En la carpeta Oferta inicial) en vez de dataUpdater.py, y se cambia una linea de código en matS.py

Control de una matriz de LEDs de acuerdo a información obtenida de www.xm.com.co

Se ejecutarán matS.py (que actualiza el estado de cada led) y dataUpdater.py (que se encarga de correr los programas para actualizar la información) en paralelo con:

sudo python3 /pathToProject/data/dataUpdater.py &

sudo python3 /pathToProject/matS.py &

Se agregarán estas dos lineas al final de /etc/profile en la raspberry para que se ejecuten al encender la raspberry

También se pueden agregar como tareas a realizar al encenderse (una mejor opción), usando esta guía:

```
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/#systemd
```

## Información de los archivos

### Centrales.xlsx

Contienen una lista con las centrales, y la información de XM

### EsquemaPCB.png

El esquema de la PCB, con el orden de las centrales

## Project

Es la carpeta que va en /home/pi de la raspberry

### matS.py

Programa que actualiza la matriz de LEDs basado en los datos que se encuentran en ./data/files/matSdata.txt

### infoWeb.py

Programa que actualiza el archivo ./data/files/infoWeb.txt ; en cada linea se muestra la informacion de la central para la hora actual, el orden es el mismo que en el archivo Centrales.xlsx

### dataUpdater.py

Se encarga de correr las funciones de los diferentes programas en ./data , así se evita que dos programas traten de editar un archivo al mismo tiempo, este prorama se corre en paralelo con matS.py

### dataTranslate.py

se encarga de tomar la información descargada en ./files/downData.txt ; tiene diferentes funciones hechas para acceder mas facilmente a la informacion

## OfertaInicial (Alternativa)

Si se desean usar los datos de Oferta inicial, y no los de Despacho nacional, se corre, de esta carpeta dataUpdaterO.py, y se actualiza matS.py

# PATH

Al pasar a la raspberry pi, actualizar los archivos dataGet , dataTranslate , infoWeb y matS con la direccion de la carpeta
