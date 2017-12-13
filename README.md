# Proyecto-Introduccion
Control de una matriz de LEDs de acuerdo a información obtenida de www.xm.com.co

Se ejecutarán matS.py (que actualiza el estado de cada led) y dataUpdater.py (que se encarga de correr los programas para actualizar la información) en paralelo con:

sudo python3 /pathToProject/data/dataUpdater.py &.
sudo python3 /pathToProject/matS.py &.

Se agregarán estas dos lineas al final de /etc/profile en la raspberry para que se ejecuten al encender la raspberry