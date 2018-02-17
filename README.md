# Proyecto Introducci�n a la Ingenier�a: Informaci�n sobre centrales de generaci�n en Colombia

El proyecto consiste, en una estructura con un mapa de Colombia, el cu�l tiene en cada punto donde hay una de las 47 centrales escogidas, un LED, el cu�l estar� encendido si la central en ese punto se encuentra en funcionamiento, y apagado si la central no est� en funcionamiento, el color del LED depende del tipo de generaci�n que se da en la central, adem�s, un panel en donde se muestra la informaci�n de generaci�n para cada central.

## Partes del proyecto

Para el desarrollo del proyecto:
1. Se edit� el mapa para agregar la ubicacion de cada central, y las convenciones.
2. Se cre� un programa en python que corre en una [Raspberri pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/).
3. Se dise�o una PCB, para controlar los 47 LEDs, con solo 16 pines ( o menos ) de la raspberry pi.
4. Se dise�o una p�gina web para mostrar los datos de generaci�n de las centrales en un panel.
5. Se dise�o una estructura para contener todos los elementos.
6. Se consiguio informaci�n sobre las centrales de xm.com.co (Archivo Centrales.xlsx)