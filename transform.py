import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucketTop = 'librostop'
    bucketPopulares = 'librospopulares'
    bucketTopPopulares = 'librostoppopulares'

    keyTop = 'librostop.json'
    keyPopulares = 'librospopulares.json'
    keyTopPopulares = 'librostoppopulares.json'

    responseTop = s3.get_object(
        Bucket=bucketTop,
        Key=keyTop,
    )

    responsePopulares = s3.get_object(
        Bucket=bucketPopulares,
        Key=keyPopulares,
    )

    # responseTop = s3.get_object(Bucket=bucketTop, key=keyTop)
    # responsePopulares = s3.get_object(Bucket=bucketPopulares, key=keyPopulares)

    contentTop = responseTop['Body']
    contentPopulares = responsePopulares['Body']

    listadoTop = json.loads(contentTop.read())
    listadoPopulares = json.loads(contentPopulares.read())

    listadoResultante = []

    dateNow = datetime.now()

    dateNow = dateNow.strftime("%m/%d/%Y, %H:%M:%S")

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
                infoLibro[
                    'endpoint'] = 'Get the Top 15 most popular books in a Month of an Year-Get the Awarded Books of a Year',
                infoLibro['download_api'] = dateNow
                listadoResultante.append(infoLibro)

    print('Resultado:', listadoResultante)

    uploadBytesStreamTopPopulares = bytes(json.dumps(listadoResultante).encode('UTF-8'))

    s3.put_object(Body=uploadBytesStreamTopPopulares, Bucket=bucketTopPopulares, Key='librostoppopulares.json')

    print("PUT top populares Success")

    return {
        'statusCode': 200,
    }
