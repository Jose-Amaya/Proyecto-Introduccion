# Configuraci�n

Para usar la p�gina con el servidor Apache, se requiere reemplazar archivos:

1. Ubicar la carpeta html en /home/pi

2. Abrir el terminal y ejecutar:
```
sudo rm /var/www/html -r
sudo mv /home/pi/html /var/www
```
## Detalles

La p�gina web usa Bootstrap framework, las librer�as de javascript jQuery y Popper, y PHP