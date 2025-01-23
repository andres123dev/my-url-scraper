# my-url-scraper  
  
<table align="center">
<tbody>
    <tr> <th>Proyect</th> <td>My URL scraper</td> </tr> <tr>
        <th>Description</th>
	<td>Terminal app to make a HTTP request to an URL and analyze the response interactively.</td>
    </tr>
      <tr> <th>Author</th> <td>Andrés Fernández Burón</td> </tr>
      <tr> <th>Copyright</th> <td>2023-2025 &copy; All rights reserved</td> </tr>
    </tbody>
  </table>
</div>

<hr>

<div id="index" align="center">  

**Language:** [Español](#index-es)   |   [English](#index-en)  
</div>

<hr>

<div id="index-es">

## Índice

1. [Descripcion](#descripcion)  
2. [Requisitos](#requisitos)  
3. [Dependencias](#dependencias)  
4. [Descarga](#descarga)  
5. [Instalacion](#instalacion)  
6. [Ejemplos de uso](#ejemplos-de-uso)
7. [Compatibilidad](#compatibilidad)  

</div>

<div id="readme-es">
<hr>  

## Descripcion  
<b>My URL scraper</b> es una aplicación de consola  que permite realizar una petición HTTP a una URL y analizar la respuesta de forma interactiva.
  
<b>My URL scraper</b> permite:
- Ver las cabeceras HTTP de la respuesta
- Ver el contenido (texto) de la respuesta
- Descargar el contenido de la respuesta
  
Si la respuesta es código HTML, también muestra la información básica del documento, y te permite:
- Buscar en el DOM, en base a una etiqueta HTML
- Buscar en el texto de la página web, un texto (case sensitive)
- Buscar en el documento, un texto (case insensitive)

## Requisitos  
<b>My URL scraper</b> está escrito con [Python](https://www.python.org/doc/), y requiere tener instalado el lenguaje [Python 3](https://www.python.org/downloads/) y [Pip]().

  
## Dependencias  
<b>My URL scraper</b> depende de los siguientes módulos Python de terceros:

- [Requests](https://requests.readthedocs.io/en/latest/)  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
- [lxml](https://lxml.de/index.html#documentation)  
- [ReportLab]()  

 Si no sabes instalar las dependencias, consulta este [manual](https://github.com/andres123dev/Apuntes-AndresFB/blob/main/python/pip.md#instalar-módulos-desde-requirementstxt).  
  
## Descarga
Puedes descargar <b>My URL scraper</b> mediante una aplicación cliente cómo ````GitBash````. 

También puedes descargarlo cómo fichero ZIP  [my-url-scraper-main.zip](https://github.com/andres123dev/my-url-scraper/archive/refs/heads/main.zip)

> Si tienes alguna duda, consulta este [manual](https://github.com/andres123dev/Apuntes-AndresFB/blob/main/github/descargar-repositorio.md).  

## Instalacion  
<b>My URL scraper</b> no necesita instalación y se ejecuta igual que cualquier otro script de Python.  

> Para ejecutar el script abre una terminal   
> y pásale al intérprete de Python,  
> la ruta al fichero ```__main__.py```  
> que se encuentra en la raíz del repositorio.  

1 - Me ubico en el directorio que contiene el repositorio:  
```cd ~\Downloads\my-url-scraper-main```  

2- <b>Si es necesario</b>, renombro el directorio del repositorio:  
```mv my-url-scraper-main my-url-scraper```  

3- Ejecuto el script  
```python my-url-scraper```  
  
## Ejemplos de uso
<b>My URL scraper</b> recibe un parámetro obligatorio: la ````URL```` a scrapear.  

```py my-url-scraper paginaweb.com```  

```py my-url-scraper http://paginaweb.com/```  

```py my-url-scraper https://paginaweb.com```  

```py my-url-scraper https://paginaweb.com/```  

```py my-url-scraper paginaweb.com/path?param1=val1&param2=val2```  
  
## Compatibilidad
<b>My URL scraper</b> es una aplicación de consola multiplataforma.

<div align="center">

| OS      | Soportado  |
|---------|------------|
| Unix    | &#10004; |
| Linux   | &#10004; |
| Windows | &#10004; |
| MAC     | Sin probar |

<br>
</div>

</div>

<div id="index-en">
<hr>

## Index  
  
1. [Description](#description)   
2. [Requirements](#requirements)  
3. [Dependencies](#dependencies)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Compatibility](#compatibility)  

</div>

<div id="readme-en">

## Description
<b>My URL scraper</b> is a terminal app to make a HTTP request to an URL and to analyze the response.  
  
<b>My URL scraper</b> allows to:
- Display the HTTP headers of the response
- Display the text content of the response
- Download the content of the response
  
Moreover, if the response is HTML code, it also displays basic information about the document, and allows you to:
- Search for a HTML tag on the DOM
- Search for a text on the text of the webpage (case sensitive)
- Search for a text on the document (case insensitive)

## Requirements
<b>My URL scraper</b> is wrote with [Python 3](https://www.python.org/downloads/), so requires to have installed [Python 3](https://www.python.org/downloads/) language and [Pip]().
  
## Dependencies

<b>My URL scraper</b> depends on the following Python third-party modules:

- [Requests](https://requests.readthedocs.io/en/latest/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [lxml](https://lxml.de/index.html#documentation)
- [ReportLab]()

> Install with Pip all the dependencies from requirements.txt  
````pip install -r requirements.txt````  
  
## Installation
<b>My URL scraper</b> doesn't need installation and runs like any other Python 3 script.  

> To run <b>My URL scraper</b> application, open a terminal  
> and give to the Python interpreter,  
> the path to the ```__main__.py``` file.   

1 - Go to the repository directory:  
```cd ~\Downloads\my-url-scraper-main```  

If is neccesary, rename the directory of the repository:  
```mv my-url-scraper-main my-url-scraper```  

3- Run the application  
```python my-url-scraper```  

## Usage
<b>My URL scraper</b> expects a required and unique parameter: the ````URL```` to scrape.  

Examples of use:

```py my-url-scraper website.com```  

```py my-url-scraper http://website.com/```  

```py my-url-scraper https://website.com```  

```py my-url-scraper https://website.com/```  

```py my-url-scraper website.com/path?param1=val1&param2=val2```  

  
## Compatibility
<b>My URL scraper</b> is a multiplatform console application.


<div align="center">  

| OS      | Compatibility |
|---------|---------------|
| Unix    | &#10004; |
| Linux   | &#10004; |
| Windows | &#10004; |
| MAC     | Not tested |
  
</div>

</div>
