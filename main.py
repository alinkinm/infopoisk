import requests
from bs4 import BeautifulSoup
import os

def download_page(url, output_folder, file_number):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.join(output_folder, f"{file_number}.html")
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(response.text)
        return file_name
    else:
        print(f"Ошибка загрузки страницы: {url}")
        return None

def create_index_file(output_folder, pages):
    index_file = os.path.join(output_folder, "index.txt")
    with open(index_file, "w", encoding="utf-8") as file:
        for i, page in enumerate(pages):
            file.write(f"{i+1}. {page}\n")


def main():
    urls = [
        "https://ilibrary.ru/text/1099/p.1/index.html",
        "https://ilibrary.ru/text/1099/p.2/index.html",
        "https://ilibrary.ru/text/1099/p.3/index.html",
        "https://ilibrary.ru/text/1099/p.4/index.html",
        "https://ilibrary.ru/text/1099/p.5/index.html",
        "https://ilibrary.ru/text/1099/p.6/index.html",
        "https://ilibrary.ru/text/1099/p.7/index.html",
        "https://ilibrary.ru/text/1099/p.8/index.html",
        "https://ilibrary.ru/text/1099/p.9/index.html",
        "https://ilibrary.ru/text/1099/p.10/index.html",
        "https://ilibrary.ru/text/1099/p.11/index.html",
        "https://ilibrary.ru/text/1099/p.12/index.html",
        "https://ilibrary.ru/text/1099/p.13/index.html",
        "https://ilibrary.ru/text/1099/p.14/index.html",
        "https://ilibrary.ru/text/1099/p.15/index.html",
        "https://ilibrary.ru/text/1099/p.16/index.html",
        "https://ilibrary.ru/text/1099/p.17/index.html",
        "https://ilibrary.ru/text/1099/p.18/index.html",
        "https://ilibrary.ru/text/1099/p.19/index.html",
        "https://ilibrary.ru/text/1099/p.20/index.html",
        "https://ilibrary.ru/text/1099/p.21/index.html",
        "https://ilibrary.ru/text/1099/p.22/index.html",
        "https://ilibrary.ru/text/1099/p.23/index.html",
        "https://ilibrary.ru/text/1099/p.24/index.html",
        "https://ilibrary.ru/text/1099/p.25/index.html",
        "https://ilibrary.ru/text/1099/p.26/index.html",
        "https://ilibrary.ru/text/1099/p.27/index.html",
        "https://ilibrary.ru/text/1099/p.28/index.html",
        "https://ilibrary.ru/text/1099/p.29/index.html",
        "https://ilibrary.ru/text/1099/p.30/index.html",
        "https://ilibrary.ru/text/1099/p.31/index.html",
        "https://ilibrary.ru/text/1099/p.32/index.html",
        "https://ilibrary.ru/text/1099/p.33/index.html",
        "https://ilibrary.ru/text/1099/p.34/index.html",
        "https://ilibrary.ru/text/1099/p.35/index.html",
        "https://ilibrary.ru/text/1099/p.36/index.html",
        "https://ilibrary.ru/text/1099/p.37/index.html",
        "https://ilibrary.ru/text/1099/p.38/index.html",
        "https://ilibrary.ru/text/1099/p.39/index.html",
        "https://ilibrary.ru/text/1099/p.40/index.html",
        "https://ilibrary.ru/text/1099/p.41/index.html",
        "https://ilibrary.ru/text/1099/p.42/index.html",
        "https://ilibrary.ru/text/1099/p.43/index.html",
        "https://ilibrary.ru/text/1099/p.44/index.html",
        "https://ilibrary.ru/text/1099/p.45/index.html",
        "https://ilibrary.ru/text/1099/p.46/index.html",
        "https://ilibrary.ru/text/1099/p.47/index.html",
        "https://ilibrary.ru/text/1099/p.48/index.html",
        "https://ilibrary.ru/text/1099/p.49/index.html",
        "https://ilibrary.ru/text/1099/p.50/index.html",
        "https://ilibrary.ru/text/1099/p.51/index.html",
        "https://ilibrary.ru/text/1099/p.52/index.html",
        "https://ilibrary.ru/text/1099/p.53/index.html",
        "https://ilibrary.ru/text/1099/p.54/index.html",
        "https://ilibrary.ru/text/1099/p.55/index.html",
        "https://ilibrary.ru/text/1099/p.56/index.html",
        "https://ilibrary.ru/text/1099/p.57/index.html",
        "https://ilibrary.ru/text/1099/p.58/index.html",
        "https://ilibrary.ru/text/1099/p.59/index.html",
        "https://ilibrary.ru/text/1099/p.60/index.html",
        "https://ilibrary.ru/text/1099/p.61/index.html",
        "https://ilibrary.ru/text/1099/p.62/index.html",
        "https://ilibrary.ru/text/1099/p.63/index.html",
        "https://ilibrary.ru/text/1099/p.64/index.html",
        "https://ilibrary.ru/text/1099/p.65/index.html",
        "https://ilibrary.ru/text/1099/p.66/index.html",
        "https://ilibrary.ru/text/1099/p.67/index.html",
        "https://ilibrary.ru/text/1099/p.68/index.html",
        "https://ilibrary.ru/text/1099/p.69/index.html",
        "https://ilibrary.ru/text/1099/p.70/index.html",
        "https://ilibrary.ru/text/1099/p.71/index.html",
        "https://ilibrary.ru/text/1099/p.72/index.html",
        "https://ilibrary.ru/text/1099/p.73/index.html",
        "https://ilibrary.ru/text/1099/p.74/index.html",
        "https://ilibrary.ru/text/1099/p.75/index.html",
        "https://ilibrary.ru/text/1099/p.76/index.html",
        "https://ilibrary.ru/text/1099/p.77/index.html",
        "https://ilibrary.ru/text/1099/p.78/index.html",
        "https://ilibrary.ru/text/1099/p.79/index.html",
        "https://ilibrary.ru/text/1099/p.80/index.html",
        "https://ilibrary.ru/text/1099/p.81/index.html",
        "https://ilibrary.ru/text/1099/p.82/index.html",
        "https://ilibrary.ru/text/1099/p.83/index.html",
        "https://ilibrary.ru/text/1099/p.84/index.html",
        "https://ilibrary.ru/text/1099/p.85/index.html",
        "https://ilibrary.ru/text/1099/p.86/index.html",
        "https://ilibrary.ru/text/1099/p.87/index.html",
        "https://ilibrary.ru/text/1099/p.88/index.html",
        "https://ilibrary.ru/text/1099/p.89/index.html",
        "https://ilibrary.ru/text/1099/p.90/index.html",
        "https://ilibrary.ru/text/1099/p.91/index.html",
        "https://ilibrary.ru/text/1099/p.92/index.html",
        "https://ilibrary.ru/text/1099/p.93/index.html",
        "https://ilibrary.ru/text/1099/p.94/index.html",
        "https://ilibrary.ru/text/1099/p.95/index.html",
        "https://ilibrary.ru/text/1099/p.96/index.html",
        "https://ilibrary.ru/text/1099/p.97/index.html",
        "https://ilibrary.ru/text/1099/p.98/index.html",
        "https://ilibrary.ru/text/1099/p.99/index.html",
        "https://ilibrary.ru/text/1099/p.100/index.html"
    ]

    output_folder = "downloaded_pages"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    downloaded_pages = []
    print("start downloading pages")
    for i, url in enumerate(urls, start=1):
        file_name = download_page(url, output_folder, i)
        if file_name:
            downloaded_pages.append(url)

    print("done downloading pages")
    create_index_file(output_folder, downloaded_pages)

if __name__ == "__main__":
    main()