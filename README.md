README – Práctica 2 (Contenerización con Docker)

En esta práctica he contenerizado la aplicación hecha en la práctica 1.3, creando una imagen Docker con todo el proyecto funcionando.
El código está dentro de la carpeta P1.3_Tienda_online y se ejecuta a través del archivo main.py.

1. Construcción de la imagen

Para construir la imagen, desde la raíz del repositorio se ejecuta:

docker build -t tienda_online:1.0 .


Esto crea la imagen usando el Dockerfile incluido en el proyecto.

2. Ejecución del contenedor

Una vez creada la imagen, la aplicación se ejecuta con:

docker run --rm tienda_online:1.0


El parámetro --rm es solo para que el contenedor se elimine automáticamente al terminar.

3. Funcionamiento de la aplicación

Cuando se ejecuta el contenedor, el programa muestra:

Los productos creados

Los pedidos de diferentes clientes

El total de cada pedido

Un histórico de pedidos

La salida es parecida a la que se obtiene al ejecutar el programa en local (productos, precios y totales).

4. Dependencias

Las dependencias están en el archivo requirements.txt.
El contenedor las instala automáticamente durante el build.

5. Estructura del repositorio
P1.3_Tienda_online/
Dockerfile
.dockerignore
requirements.txt
README.md

6. Notas sobre el repositorio y Git

El trabajo de Docker se hizo en la rama feature/docker.

Después se abrió un Pull Request y se fusionó a main.

En la rama main está ahora la versión final del proyecto.
