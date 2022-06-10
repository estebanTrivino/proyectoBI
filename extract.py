import json

import requests
from datetime import datetime

# Lambda 1 - Extraction Function
def extraction():
    year = 2021
    month = 3

    # Libros premiados en el 2021
    urlTop2021 = 'https://hapi-books.p.rapidapi.com/top/{}'.format(year)

    headersTop2021 = {
        "X-RapidAPI-Key": "74e5961d04msh950dbf4ea45ae4ep1aaeb0jsnf15500141925",
        "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
    }

    listadoTop = requests.request("GET", urlTop2021, headers=headersTop2021)
    listadoTop = json.loads(listadoTop.text)
    print("Listado de libros ganadores de premios en el año seleccionado: ", listadoTop)

    # Los 15 libros más populares en marzo de 2022
    urlPopulares = 'https://hapi-books.p.rapidapi.com/month/{}/{}'.format(year, month)

    headersPopulares = {
        "X-RapidAPI-Key": "74e5961d04msh950dbf4ea45ae4ep1aaeb0jsnf15500141925",
        "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
    }

    listadoPopulares = requests.request("GET", urlPopulares, headers=headersPopulares)
    listadoPopulares = json.loads(listadoPopulares.text)
    print('Listado Libros Populares', listadoPopulares)

    # Categoria y titulo de los libros más populares en un mes x de un año x que han sido premiados en ese año
    listadoResultante = []

    for libro in listadoTop:
        for libroP in listadoPopulares:
            if int(libro['book_id']) == int(libroP['book_id']):
                infoLibro = {}
                infoLibro['book_id'] = libro['book_id']
                infoLibro['winning_category'] = libro['winning_category']
                infoLibro['name'] = libro['name']
                infoLibro['anio'] = 2015
                infoLibro['mes'] = 5
                infoLibro['api'] = 'HapiBooks'
                infoLibro['endPoints'] = ['Get the Top 15 most popular books in a Month of an Year',
                                          'Get the Awarded Books of a Year']
                infoLibro['fechaConsulta'] = datetime.now()
                listadoResultante.append(infoLibro)
    print('Resultado:', listadoResultante)