from olclient.openlibrary import OpenLibrary
import olclient.common as common
import requests
import time

import psycopg2

def search_book_by_title(title):
    url = f"https://openlibrary.org/search.json"
    params = {
        'title': title,
        'limit': 20
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['docs']
    else:
        print("Error al conectar con OpenLibrary API")
        return []

title = "Rebelión en la granja" 
start = time.time()
results = search_book_by_title(title)
end = time.time()
print(f"Tiempo de búsqueda: {end - start:.2f} segundos")

for book in results[1:5]:
    print(f"Título: {book.get('title')}")
    print(f"Autor: {book.get('author_name', 'Autor no disponible')}")
    print(f"Año de publicación: {book.get('first_publish_year', 'Año no disponible')}")
    print(f"ISBN: {book.get('isbn', 'ISBN no disponible')}")
    print()