import pandas as pd
import requests as req
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def get_bank_sites(url: str):
    page = req.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    })
    base_url = urlparse(url).scheme + "://" + urlparse(url).netloc
    soup = BeautifulSoup(page.content, 'html.parser')
    finds = soup.find_all('a', href=True)
    finds = [find for find in finds if find['href'] != '#']
    lokats = []
    for find in finds:
        parent = find.parent.parent
        for child in parent.children:
            if "lokat" in child.text.lower() and any(x in child.text.lower() for x in ("tabel", "regul")) and \
                    not any(ill in child.text.lower() for ill in ("kredyt", "regulamin")):
                if find['href'].startswith("/"):
                    lokats.append(base_url + find['href'])
                else:
                    lokats.append(find['href'])
    return lokats


def main():
    sites = pd.read_csv(open("bank_sites.csv"), delimiter=";")
    sites['Osoby fizyczne'] = sites['Osoby fizyczne'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    sites['Klienci korporacyjni'] = sites['Klienci korporacyjni'].apply(
        lambda x: x.strip() if isinstance(x, str) else x)
    locats = []
    for record in sites['Osoby fizyczne'].dropna():
        for site in record.split(" ") if " " in record else [record]:
            locats.extend(get_bank_sites(site))
    temp = []
    for loc in set(locats):
        try:
            parsed = urlparse(loc)
            if not loc.endswith(parsed.netloc):
                temp.append(loc)
        except ValueError:
            pass
    locats = temp
    print(locats)
    # get_bank_sites('https://www.velobank.pl/klienci-indywidualni/centrum-dokumentow')


if __name__ == "__main__":
    main()

# .pdf -> tabela oprocentowanie -> levenstein / regex -> END!
# .pdf -> look inside?
# ask which text is the most probable to show .pdf -> get text to click -> click ahref -> get .pdf -> END!
# click every ahref to show everything -> tabela oprocentowanie -> levenstein / regex -> END!
