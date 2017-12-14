# Proyecto-Introduccion

Los archivos principales se encuentran en la carpeta "project"

Se planean utilizar los datos de Despacho Nacional, pero si es necesario, se pueden utilizar los datos de Oferta inicial, para esto se ejecuta dataUpdaterO.py (En la carpeta Oferta inicial) en vez de dataUpdater.py, y se cambia una linea de código en matS.py

Control de una matriz de LEDs de acuerdo a información obtenida de www.xm.com.co

Se ejecutarán matS.py (que actualiza el estado de cada led) y dataUpdater.py (que se encarga de correr los programas para actualizar la información) en paralelo con:

sudo python3 /pathToProject/data/dataUpdater.py &

sudo python3 /pathToProject/matS.py &

Se agregarán estas dos lineas al final de /etc/profile en la raspberry para que se ejecuten al encender la raspberry