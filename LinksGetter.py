# Klasa służąca do wczytywania danych z pliku
import re


class CSVReader:
    # Utworzenie listy list (tabeli) danych na podstawie pliku
    @staticmethod
    def readCSV(path: str, split: str = ","):
        with open(path) as file:
            text = file.read()
        return [line.split(split) for line in text.splitlines()]


class LinksGetter:
    @staticmethod
    def getLink(text: str):
        regex = re.compile(r'https:.+$')
        br = re.compile(r'\[.*\]')
        text = re.sub(br, "", text)
        links: list[str] = regex.findall(text)
        link = links[0]
        links = link.split("https:")
        links = ["https:" + link for link in links]
        return [link for link in links[1:] if len(link) != 0]


class PercLink:
    def __init__(self, name: str, fiz: list, corp: list):
        self.name = name
        self.fiz = list(set(fiz))
        self.corpo = list(set(corp))

    def __str__(self):
        return self.name + "\n" + str(self.fiz) + "\n" + str(self.corpo) + "\n========"

    @staticmethod
    def getBanksFromTable():
        csv = CSVReader.readCSV("tabele_oprocentowania.csv", split=";")
        NAME_INDEX: int = 1
        RIZZ_INDEX: int = 2
        CORPO_INDEX: int = 3
        percLinks = []
        for i, row in enumerate(csv):
            try:
                percLinks.append(PercLink(row[NAME_INDEX],
                                          LinksGetter.getLink(row[RIZZ_INDEX]),
                                          LinksGetter.getLink(row[CORPO_INDEX] if len(row) > CORPO_INDEX else "")))
            except IndexError:
                pass
        return percLinks
