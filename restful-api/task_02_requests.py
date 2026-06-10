#!/usr/bin/python3
"""Module Consuming and processing data from an API using Python"""


import requests
import csv

def fetch_and_print_posts():  # affiche les titres dans le terminal
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():  # sauvegarde id, title, body dans un fichier CSV
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        structured = [
            {
                "id": element["id"],
                "title": element["title"],
                "body": element["body"]
            }
                for element in posts
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()      # écrit la ligne d'en-tête
            writer.writerows(structured)     # écrit toutes les lignes
