# Proyecto-Introduccion

Los archivos principales se encuentran en la carpeta "project", esta carpeta debe ir en el directorio 'home/pi' de la Raspberry Pi

Se planean utilizar los datos de Despacho Nacional, pero si es necesario, se pueden utilizar los datos de Oferta inicial, para esto se ejecuta dataUpdaterO.py (En la carpeta Oferta inicial) en vez de dataUpdater.py, y se cambia una linea de código en matS.py

# Requisitos

Una memoria SD, de al menos 8GB, y preferiblemente de clase 10, para el sistema operativo

Para correr los programas en la Raspberry pi 3, Se necesita el sistema operativo [Raspbian -(version Jessie)](https://www.raspberrypi.org/downloads/raspbian/),se necesita de [Python3.5](https://www.python.org/downloads/release/python-350/), y tener la [librería Pycurl](http://pycurl.io/) instalada, y para la página web, se necesita de el servidor HTTP [Apache](https://httpd.apache.org/download.cgi) y de [PHP](http://php.net/downloads.php)

1. Instalar Raspbian:
1. Descargar [RASPBIAN STRETCH WITH DESKTOP](https://www.raspberrypi.org/downloads/raspbian/)
2. Descargar [Etcher](https://etcher.io/)
3. Seguir las instrucciones de la página de [Etcher](https://etcher.io/) para instalar el sistema operativo en la memoria SD

2. Instalar Python3.5:
1. Abrir el terminal y ejecutar:
```
sudo apt-get install python3.5
```

3. Instalar la librería Pycurl:
1. Abrir el terminal y ejecutar:
```
sudo pip install pycurl
```
2. Si la ejecución falla, ejecutar:
```
sudo apt-get install python-pip
```
y ejecutar 3.1. denuevo



## Ejecución

Se ejecutarán matS.py (que actualiza el estado de cada led) y dataUpdater.py (que se encarga de correr los programas para actualizar la información) en paralelo, para configurar los programas para que corran al encender la Raspberry, se realizaron estos pasos:

1. Abrir el terminal y ejecutar:

```
sudo nano /lib/systemd/system/matS.service
```

2. Escribir:

```
 [Unit]
 Description=MatS
 After=multi-user.target

 [Service]
 Type=idle
 ExecStart=/usr/bin/python3.5 /home/pi/sample.py

 [Install]
 WantedBy=multi-user.target
 ```



Guía usada: https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/#systemd

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
