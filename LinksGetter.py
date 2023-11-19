import re


class FileReader:
    # Create data table from file
    @staticmethod
    def create_table_from(path: str, split: str = ","):
        with open(path) as file:
            text = file.read()
        return [line.split(split) for line in text.splitlines()]


class LinksGetter:
    # Get all and only URL from text
    @staticmethod
    def get_all_url_from(text: str):
        regex = re.compile(r'https:.+$')
        br = re.compile(r'\[.*\]')
        text = re.sub(br, "", text)
        links: list[str] = regex.findall(text)
        link = links[0]
        links = link.split("https:")
        links = ["https:" + link for link in links]
        return [link for link in links[1:] if len(link) != 0]


class BankData:
    def __init__(self, bank_name: str, private_offer: list, business_offer: list):
        self.bank_name = bank_name
        self.private_offer = list(set(private_offer))
        self.corporate = list(set(business_offer))

    def __str__(self):
        return self.bank_name + "\n" + str(self.private_offer) + "\n" + str(self.corporate) + "\n========"
    # Get all bank's urls
    @staticmethod
    def get_banks_data_url_from_table():
        BANK_NAME_INDEX: int = 1
        PRIVATE_OFFER_INDEX: int = 2
        BUSINESS_OFFER_INDEX: int = 3
        TABLE_PATH = "tabele_oprocentowania.csv"
        csv = FileReader.create_table_from(TABLE_PATH, split=";")
        banks_data_urls = []
        for row in csv:
            try:
                banks_data_urls.append(BankData(row[BANK_NAME_INDEX],
                                          LinksGetter.get_all_url_from(row[PRIVATE_OFFER_INDEX]),
                                          LinksGetter.get_all_url_from(row[BUSINESS_OFFER_INDEX] if len(row) > BUSINESS_OFFER_INDEX else "")))
            except IndexError:
                pass
        return banks_data_urls