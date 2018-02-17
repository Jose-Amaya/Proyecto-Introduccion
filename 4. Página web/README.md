# Configuración

Para usar la página con el servidor Apache, se requiere reemplazar archivos:

1. Ubicar la carpeta html en /home/pi

2. Abrir el terminal y ejecutar:
```
sudo rm /var/www/html -r
sudo mv /home/pi/html /var/www
```
## Detalles

La página web usa Bootstrap framework, las librerías de javascript jQuery y Popper, y PHP