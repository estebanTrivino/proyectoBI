import requests

# Lambda 1 - Extraction Function

year = 2021
month = 3

# Libros premiados en el 2021
urlTop2021 = 'https://hapi-books.p.rapidapi.com/top/{}'.format(year)
print(urlTop2021)
headersTop2021 = {
    "X-RapidAPI-Key": "74e5961d04msh950dbf4ea45ae4ep1aaeb0jsnf15500141925",
    "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
}
responseTop2021 = requests.request("GET", urlTop2021, headers=headersTop2021)
print(responseTop2021.text)

# Los 15 libros más populares en marzo de 2022
urlPopulares = 'https://hapi-books.p.rapidapi.com/month/{}/{}'.format(year, month)
print(urlPopulares)
headersPopulares = {
    "X-RapidAPI-Key": "74e5961d04msh950dbf4ea45ae4ep1aaeb0jsnf15500141925",
    "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
}
responsePopulares = requests.request("GET", urlPopulares, headers=headersPopulares)
print(responsePopulares.text)
