#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__name__ =        "scrape"
__description__ = "Functions to request a URL and handle the response."
__date__ =        "14-06-2022"
__author__ =      "Andrés Fernández Burón"
__copyright__ =   "Copyright 2022-2025"
__license__ =     "All rights reserved"
__version__ =     "0.1"
__status__ =      "Production"
__maintainer__ =  "Andrés Fernández Burón"
__email__ =       "https://github.com/AndresFernandezBuron/scrape-uri/issues/new/choose"
    
import requests

from .files import *
from .menu import *

# ------------------------------------------------------------------------------
# DEVUELVO LA URI NORMALIZADA
# ------------------------------------------------------------------------------
def normalize_URI( URI ):
    URI = URI.strip(' ')
    if( not URI.startswith('http') ):
        URI = f"http://{URI}"
    if( not URI.endswith('/') ):
        URI = f"{URI}/"
    return URI

# ------------------------------------------------------------------------------
# HAGO UNA PETICIÓN A UNA URI Y DEVUELVO EL CONTENIDO DE LA RESPUESTA O NONE
# ------------------------------------------------------------------------------
def scrap_URI( URI ):
    content = None
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    try:
        content = requests.get(URI, params={}, headers={'User-Agent': user_agent})
        return content
    except Exception as e:
        print(f"\n Error al hacer la petición !!\n\n {e}\n")
        exit()

# ------------------------------------------------------------------------------
# DEVUELVO EL STR DE UN TAG DE BS4 SIN ESPACIOS BLANCOS GRANDES
# ------------------------------------------------------------------------------
def strip_whitespaces( tag ):
    tag = str( tag )
    tag = tag.strip()
    tag = tag.replace('  ', ' ')
    tag = tag.replace('\n', ' ')
    tag = tag.replace('\t', ' ')
    return tag
