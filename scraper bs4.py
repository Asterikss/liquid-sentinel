import pandas as pd
import requests as req
from bs4 import BeautifulSoup


def get_bank_sites(url: str):
    page = req.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    })
    soup = BeautifulSoup(page.content, 'html.parser')
    finds = soup.find_all('a', href=True)
    finds = [find for find in finds if find['href'] != '#']
    lokats = []
    for find in finds:
        parent = find.parent.parent
        for child in parent.children:
            if "lokat" in child.text.lower() and any(x in child.text.lower() for x in ("regul", "tabel")):
                lokats.append("https://www.bankmillennium.pl"+find['href'])
    print(lokats)


def main():
    # sites = pd.read_csv(open("bank_sites.csv"), delimiter=";")
    # sites['Osoby fizyczne'] = sites['Osoby fizyczne'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    # sites['Klienci korporacyjni'] = sites['Klienci korporacyjni'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    # for record in sites['Osoby fizyczne'].dropna():
    #     for site in record.split(" ") if " " in record else [record]:
    #         get_bank_sites(site)
    get_bank_sites('https://www.bankmillennium.pl/klienci-indywidualni/wsparcie/cenniki-i-regulaminy')


if __name__ == "__main__":
    main()
