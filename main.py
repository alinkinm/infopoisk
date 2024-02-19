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
        "https://en.wikipedia.org/wiki/Vladimir_Putin",
        "https://en.wikipedia.org/wiki/Brad_Pitt",
        "https://en.wikipedia.org/wiki/Ryan_Reynolds",
        "https://en.wikipedia.org/wiki/Charles_Manson",
        "https://en.wikipedia.org/wiki/John_Cena",
        "https://en.wikipedia.org/wiki/Princess_Margaret,_Countess_of_Snowdon",
        "https://en.wikipedia.org/wiki/Israel",
        "https://en.wikipedia.org/wiki/Nicki_Minaj",
        "https://en.wikipedia.org/wiki/Bruce_Lee",
        "https://en.wikipedia.org/wiki/Winston_Churchill",
        "https://en.wikipedia.org/wiki/Wikipedia:Contact_us",
        "https://en.wikipedia.org/wiki/Bill_Gates",
        "https://en.wikipedia.org/wiki/Earth",
        "https://en.wikipedia.org/wiki/Singapore",
        "https://en.wikipedia.org/wiki/Jay-Z",
        "https://en.wikipedia.org/wiki/Tom_Brady",
        "https://en.wikipedia.org/wiki/Titanic",
        "https://en.wikipedia.org/wiki/William_Shakespeare",
        "https://en.wikipedia.org/wiki/Manchester_United_F.C.",
        "https://en.wikipedia.org/wiki/Mark_Zuckerberg",
        "https://en.wikipedia.org/wiki/Vietnam_War",
        "https://en.wikipedia.org/wiki/Mila_Kunis",
        "https://en.wikipedia.org/wiki/Pablo_Escobar",
        "https://en.wikipedia.org/wiki/Ted_Bundy",
        "https://en.wikipedia.org/wiki/Will_Smith",
        "https://en.wikipedia.org/wiki/Muhammad_Ali",
        "https://en.wikipedia.org/wiki/Meghan,_Duchess_of_Sussex",
        "https://en.wikipedia.org/wiki/Breaking_Bad",
        "https://en.wikipedia.org/wiki/Jennifer_Aniston",
        "https://en.wikipedia.org/wiki/Ariana_Grande",
        "https://en.wikipedia.org/wiki/France",
        "https://en.wikipedia.org/wiki/Chernobyl_disaster",
        "https://en.wikipedia.org/wiki/How_I_Met_Your_Mother",
        "https://en.wikipedia.org/wiki/Arnold_Schwarzenegger",
        "https://en.wikipedia.org/wiki/Keanu_Reeves",
        "https://en.wikipedia.org/wiki/Marilyn_Monroe",
        "https://en.wikipedia.org/wiki/Diana,_Princess_of_Wales",
        "https://en.wikipedia.org/wiki/COVID-19_pandemic",
        "https://en.wikipedia.org/wiki/John_F._Kennedy",
        "https://en.wikipedia.org/wiki/Jeffrey_Dahmer",
        "https://en.wikipedia.org/wiki/Queen_Victoria",
        "https://en.wikipedia.org/wiki/Angelina_Jolie",
        "https://en.wikipedia.org/wiki/Tupac_Shakur",
        "https://en.wikipedia.org/wiki/Lil_Wayne",
        "https://en.wikipedia.org/wiki/Scarlett_Johansson",
        "https://en.wikipedia.org/wiki/The_Walking_Dead_(TV_series)",
        "https://en.wikipedia.org/wiki/Elvis_Presley",
        "https://en.wikipedia.org/wiki/Harry_Potter",
        "https://en.wikipedia.org/wiki/Prince_Philip,_Duke_of_Edinburgh",
        "https://en.wikipedia.org/wiki/Academy_Awards",
        "https://en.wikipedia.org/wiki/Albert_Einstein",
        "https://en.wikipedia.org/wiki/Rihanna",
        "https://en.wikipedia.org/wiki/Tom_Cruise",
        "https://en.wikipedia.org/wiki/Joe_Biden",
        "https://en.wikipedia.org/wiki/Selena_Gomez",
        "https://en.wikipedia.org/wiki/Kobe_Bryant",
        "https://en.wikipedia.org/wiki/Leonardo_DiCaprio",
        "https://en.wikipedia.org/wiki/September_11_attacks",
        "https://en.wikipedia.org/wiki/Germany",
        "https://en.wikipedia.org/wiki/Miley_Cyrus",
        "https://en.wikipedia.org/wiki/Star_Wars",
        "https://en.wikipedia.org/wiki/Darth_Vader",
        "https://en.wikipedia.org/wiki/Charles_III",
        "https://en.wikipedia.org/wiki/LeBron_James",
        "https://en.wikipedia.org/wiki/Abraham_Lincoln",
        "https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films",
        "https://en.wikipedia.org/wiki/Kanye_West",
        "https://en.wikipedia.org/wiki/Japan",
        "https://en.wikipedia.org/wiki/New_York_City",
        "https://en.wikipedia.org/wiki/Russia",
        "https://en.wikipedia.org/wiki/Malware",
        "https://en.wikipedia.org/wiki/XXXX",
        "https://en.wikipedia.org/wiki/Portal:Contents",
        "https://en.wikipedia.org/wiki/China",
        "https://en.wikipedia.org/wiki/List_of_highest-grossing_films",
        "https://en.wikipedia.org/wiki/Stephen_Hawking",
        "https://en.wikipedia.org/wiki/Search_engine",
        "https://en.wikipedia.org/wiki/Taylor_Swift",
        "https://en.wikipedia.org/wiki/The_Big_Bang_Theory",
        "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States",
        "https://en.wikipedia.org/wiki/Australia",
        "https://en.wikipedia.org/wiki/Michael_Jordan",
        "https://en.wikipedia.org/wiki/Dwayne_Johnson",
        "https://en.wikipedia.org/wiki/Steve_Jobs",
        "https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License",
        "https://en.wikipedia.org/wiki/Johnny_Depp",
        "https://en.wikipedia.org/wiki/Kim_Kardashian",
        "https://en.wikipedia.org/wiki/Freddie_Mercury",
        "https://en.wikipedia.org/wiki/Canada",
        "https://en.wikipedia.org/wiki/Justin_Bieber",
        "https://en.wikipedia.org/wiki/The_Beatles",
        "https://en.wikipedia.org/wiki/World_War_I",
        "https://en.wikipedia.org/wiki/Game_of_Thrones",
        "https://en.wikipedia.org/wiki/Lionel_Messi",
        "https://en.wikipedia.org/wiki/Eminem",
        "https://en.wikipedia.org/wiki/Adolf_Hitler",
        "https://en.wikipedia.org/wiki/Lady_Gaga",
        "https://en.wikipedia.org/wiki/Cleopatra",
        "https://en.wikipedia.org/wiki/Elon_Musk",
        "https://en.wikipedia.org/wiki/Michael_Jackson"
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