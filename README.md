# Proyecto Introducción a la Ingeniería: Información sobre centrales de generación en Colombia

El proyecto consiste, en una estructura con un mapa de Colombia, el cuál tiene en cada punto donde hay una de las 47 centrales escogidas, un LED, el cuál estará encendido si la central en ese punto se encuentra en funcionamiento, y apagado si la central no está en funcionamiento, el color del LED depende del tipo de generación que se da en la central, además, un panel en donde se muestra la información de generación para cada central.

## Partes del proyecto

Para el desarrollo del proyecto:
1. Se editó el mapa para agregar la ubicacion de cada central, y las convenciones. [Carpeta](1. Diseño mapa)
2. Se creó un programa en python que corre en una [Raspberri pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/). [Carpeta](2. Programación)
3. Se diseño una PCB, para controlar los 47 LEDs, con solo 16 pines ( o menos ) de la raspberry pi. [Carpeta](3. PCB)
4. Se diseño una página web para mostrar los datos de generación de las centrales en un panel. [Carpeta](4. Página web)
5. Se diseño una estructura para contener todos los elementos. [Carpeta](4. Estructura)
6. Se consiguio información sobre las centrales de xm.com.co (Archivo Centrales.xlsx)