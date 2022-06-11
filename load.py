import json
import boto3
import pymysql


def lambda_handler(event, context):
    s3 = boto3.client('s3', )

    bucketTopPopulares = 'librostoppopulares'

    keyTopPopulares = 'librostoppopulares.json'

    responseTopPopulares = s3.get_object(
        Bucket=bucketTopPopulares,
        Key=keyTopPopulares,
    )

    contentTopPopulares = responseTopPopulares['Body']

    listadoTopPopulares = json.loads(contentTopPopulares.read())

    for item in (listadoTopPopulares):
        libro = (
            str(item['book_id']), str(item['name']), str(item['mes']),
            str(item['anio']), str(item['api']), str(item['end']), str(item['download_api'])
        )
        conn = pymysql.connect(host='databasebi-1.crdaxhn2501g.us-east-2.rds.amazonaws.com', user='admin',
                               passwd='bi123456789', db='databasebooks')
        cursor = conn.cursor()
        pymysql_insert = cursor.execute(
            "INSERT INTO librosTopPopulares(idbook, name, mes, anio, api, endpoint, download_api) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            libro)
        conn.commit()

    cursor.close()
    conn.close()

    return {
        'statusCode': 200,
    }
