# my-url-scraper  
  
<table align="center">
<tbody>
    <tr>
        <th>Proyect</th>
        <td>my-url-scraper</td>
    </tr>
    <tr>
        <th>Description</th>
		<td>Interactive terminal app to make a HTTP request to an URL and analyze the response.</td>
    </tr>
	<tr>
		<th>Author</th>
		<td>Andrés Fernández Burón</td>
	</tr>
	<tr>
		<th>Copyright</th>
		<td>2022-2025 &copy; All rights reserved</td>
	</tr>
</tbody>
</table>

<hr>

<div id="index" align="center">
	<b>Language:</b> <a href="#index-es">Español</a> | <a href="#index-en">English</a>
</div>

<hr>

<div id="index-es">

## Índice

- Descripción
- Requisitos
- Dependencias
- Instalación
- Ejemplos de uso
- Compatibilidad

</div>

<div id="readme-es">
<hr>  

## Descripción  
<b>My URL scraper</b> es una aplicación de consola escrita con <a href="https://www.python.org/doc/" target="_blank">Python 3</a>, que permite realizar una petición HTTP a una URL y analizar la respuesta de forma interactiva.
  
<b>My URL scraper</b> te permite:
- Ver las cabeceras HTTP de la respuesta
- Ver el contenido (texto) de la respuesta
- Descargar el contenido de la respuesta
  
Si la respuesta es código HTML, también muestra la información básica del documento, y te permite:
- Buscar en el DOM, en base a una etiqueta HTML
- Buscar en el texto de la página web, un texto (case sensitive)
- Buscar en el documento, un texto (case insensitive)

## Requisitos  
<b>My URL scraper</b> requiere tener instalado <a href="https://www.python.org/downloads/" target="_blank">Python 3</a> y <a href="" target="_blank">Pip</a>.
  
## Dependencias  
<b>My URL scraper</b> depende de los siguientes módulos Python de terceros:

- <a href="https://requests.readthedocs.io/en/latest/" target="_blank">Requests</a>
- <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">BeautifulSoup4</a>
- <a href="https://lxml.de/index.html#documentation" target="_blank">lxml</a>

Instalar las dependencias manualmente con Pip:  
<code> pip install request, bs4, reportlab </code>  

Instalar las dependencias desde requirements.txt:  
<code> pip install -r requiremnts.txt </code>
  
## Instalación  
<b>My URL scraper</b> no necesita instalación.  
  
## Ejemplos de uso
<b>My URL scraper</b> se ejecuta cómo cualquier script de Python 3.  

Recibe un parámetro obligatorio: la URL a scrapear.  
  
Ejemplos de uso:  

<code> python my-url-scraper paginaweb.com </code>  
<code> python my-url-scraper http://paginaweb.com </code>  

<code> python my-url-scraper https://paginaweb.com/ </code>  
<code> python my-url-scraper https://www.paginaweb.com/ </code>  

<code> python my-url-scraper webpage.com/path?param1=val1&param2=val2 </code>  
  
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

- Description
- Requirements
- Dependencies
- Installation
- Examples of usage
- Compatibility

</div>

<div id="readme-en">

## Description
<b>My URL scraper</b> is a terminal app wrote with <a href="https://www.python.org/downloads/" target="_blank">Python 3</a>, to make a HTTP request to an URL and to analyze the response.  
  
<b>My URL scraper</b> allows you to:
- Display the HTTP headers of the response
- Display the text content of the response
- Download the content of the response
  
If the response is HTML code, it also displays basic information about the document, and allows you to:
- Search for a HTML tag on the DOM
- Search for a text on the text of the webpage (case sensitive)
- Search for a text on the document (case insensitive)

## Requirements
<b>My URL scraper</b> requires to have intalled <a href="https://www.python.org/downloads/" target="_blank">Python 3</a> and <a href="">Pip</a>.
  
## Dependencies

<b>My URL scraper</b> depends on the following Python third party modules:

- <a href="https://requests.readthedocs.io/en/latest/" target="_blank">requests</a>
- <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">bs4</a>
- <a href="https://lxml.de/index.html#documentation">lxml</a>

Install the dependencies manually with Pip:  
<code> pip install request, bs4, reportlab </code>  

Or install all dependencies from requirements.txt:  
<code> pip install -r requirements.txt </code>  
  
## Installation
<b>My URL scraper</b> doesn't need installation.  

## Usage
<b>My URL scraper</b> runs like any other Python 3 script.  

It expects a single required parameter: the URL to scrape.  

Usage example:  

<code> python my-url-scraper webpage.com</code>  
<code> python my-url-scraper http://webpage.com</code>  

<code> python my-url-scraper https://www.webpage.com/</code>  
<code> python my-url-scraper https://webpage.com/</code>  

<code> python my-url-scraper webpage.com/path?param1=val1&param2=val2</code>  

  
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
