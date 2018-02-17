# Proyecto-Introduccion

Los archivos principales se encuentran en la carpeta "project", esta carpeta debe ir en el directorio 'home/pi' de la Raspberry Pi

Se planean utilizar los datos de Despacho Nacional, pero si es necesario, se pueden utilizar los datos de Oferta inicial, para esto se cambia una linea de código en matS.py

# Requisitos

Una memoria SD, de al menos 8GB, y preferiblemente de clase 10, para el sistema operativo

Para correr los programas en la Raspberry pi 3, Se necesita el sistema operativo [Raspbian (version Jessie)](https://www.raspberrypi.org/downloads/raspbian/),se necesita de [Python3.5](https://www.python.org/downloads/release/python-350/), y tener la [librería Pycurl](http://pycurl.io/) instalada, y para la página web, se necesita de el servidor HTTP [Apache](https://httpd.apache.org/download.cgi) y también se necesita de el módulo de PHP para el servidor

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

4. Instalar el servidor HTTP Apache:
	1. Abrir el terminal y ejecutar:
	```
	sudo apt-get install apache2 -y
	```

5. Instalar el módulo PHP:
	1. Abrir el terminal y ejecutar:
	```
	sudo apt-get install php libapache2-mod-php -y
	```

Guias de referencia:
* https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md

## Ejecución

Se ejecutarán matS.py (que actualiza el estado de cada led), dataUpdater.py (que se encarga de correr las funciones para actualizar la información) y dataUpdaterO.py en paralelo, para configurar los programas para que corran al encender la Raspberry, se realizaron estos pasos:

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
 ExecStart=/usr/bin/python3.5 /home/pi/project/matS.py
 Restart=always
 RestartSec=5

 [Install]
 WantedBy=multi-user.target
```

3. Presionar en orden las teclas / combinaciones de teclas:
```
CTRL + X
Y
ENTER
```

1. Abrir el terminal y ejecutar:
```
sudo nano /lib/systemd/system/dataUpdater.service
```

2. Escribir:
```
 [Unit]
 Description=DataUpdater
 After=network.target

 [Service]
 Type=idle
 ExecStart=/usr/bin/python3.5 /home/pi/project/data/dataUpdater.py
 Restart=always
 RestartSec=5

 [Install]
 WantedBy=multi-user.target
```

3. Presionar en orden las teclas / combinaciones de teclas:
```
CTRL + X
Y
ENTER
```

1. Abrir el terminal y ejecutar:
```
sudo nano /lib/systemd/system/dataUpdaterO.service
```

2. Escribir:
```
 [Unit]
 Description=DataUpdaterO
 After=network.target

 [Service]
 Type=idle
 ExecStart=/usr/bin/python3.5 /home/pi/project/data/OfertaInicial(Alternativa)/dataUpdaterO.py
 Restart=always
 RestartSec=5

 [Install]
 WantedBy=multi-user.target
```

3. Presionar en orden las teclas / combinaciones de teclas:
```
CTRL + X
Y
ENTER
```

1. En el terminal ejecutar ( una linea a la vez ):
```
sudo chmod 644 /lib/systemd/system/matS.service
sudo chmod 644 /lib/systemd/system/dataUpdater.service
sudo chmod 644 /lib/systemd/system/dataUpdaterO.service

sudo systemctl daemon-reload

sudo systemctl enable matS.service
sudo systemctl enable dataUpdater.service
sudo systemctl enable dataUpdaterO.service

sudo reboot
```

Guias de referencia:
* https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/#systemd
* https://www.raspberrypi.org/documentation/linux/usage/systemd.md
* https://www.freedesktop.org/software/systemd/man/systemd.service.html

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

## OfertaInicial(Alternativa)

Si se desean usar los datos de Oferta inicial, y no los de Despacho nacional, se corre, de esta carpeta dataUpdaterO.py, y se actualiza matS.py

# PATH

Al pasar a la raspberry pi, actualizar los archivos dataGet , dataTranslate , infoWeb y matS con la direccion de la carpeta
