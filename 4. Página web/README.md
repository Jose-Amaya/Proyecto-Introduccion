# Configuración

Para usar la página con el servidor Apache, se requiere reemplazar archivos:

1. Mover la carpeta html a /home/pi

2. Abrir el terminal y ejecutar:
```
sudo rm /var/www/html -r
sudo mv /home/pi/html /var/www
```
## Detalles

La página web usa [Bootstrap framework](https://getbootstrap.com/), las librerías de javascript [jQuery](https://jquery.com/) y [Popper](https://popper.js.org/), y [PHP](http://www.php.net/)
