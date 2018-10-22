# Código fuente de la revista de SciPyLA

Éste repositorio contiene el código fuente de la revista de SciPyLA

 
## Cómo generar el contenido del Blog

Para crear el contenido estático del blog se necesita tener instalado [pelican](http://docs.getpelican.com/en/stable/)

1. Clona este repositorio  

```
$ git clone https://github.com/scipy-latinamerica/revista.io.git
$ cd revista.io/

```

2. Guarda el notebook que quieres publicar en la carpeta content/notebooks


3. Genera el archivo `markdown` en la carpeta content con la siguiente estructura:

```
Title: título del artículo
Date: fecha de publicacion
Category: categoria en la que se incluye el artículo
Tags: tags relevantes
Author: nombre del autor
Description: una breve descripción del artículo

{% notebook nombreDelNotebook.ipynb cells[2:] %}
```
ver los ejemplos para tomar de referencia

4. Genera el html estático y sirvelo localmente con `Pelican`:

```
$ make html && make serve
$ open http://localhost:8000
```

5. Despliega a Github Pages 
