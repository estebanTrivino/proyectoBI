import json
import requests
import boto3  # Libreria necesaria para usar los productos de aws

s3 = boto3.client('s3')  # Se instancia el recurso del s3


def lambda_handler(event, context):
    bucketTop = 'librostop'
    bucketPopulares = 'librospopulares'

    fileTop = 'librostop.json'
    filePopulares = 'librospopulares.json'

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

    uploadBytesStreamTop = bytes(json.dumps(listadoTop).encode('UTF-8'))
    uploadBytesStreamPopulares = bytes(json.dumps(listadoPopulares).encode('UTF-8'))

    s3.put_object(Body=uploadBytesStreamTop, Bucket=bucketTop, Key=fileTop)

    print('PUT Top Success')

    s3.put_object(Body=uploadBytesStreamPopulares, Bucket=bucketPopulares, Key=filePopulares)

    print('PUT Populares Success')

    return {
        'statusCode': 200,
    }
