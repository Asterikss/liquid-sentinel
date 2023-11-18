from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

import LinksGetter


class WebScrapper:
    EDGE_PATH = 'edgedriver_win64/msedgedriver.exe'

    def __init__(self, url: str):
        self.driver = webdriver.Edge(executable_path=WebScrapper.EDGE_PATH)
        self.driver.get(url)

if __name__ == "__main__":
    banks = LinksGetter.PercLink.getBanksFromTable()
    for bank in banks:
        print(bank)
    bank = banks[0]
    ws = WebScrapper(bank.fiz[0])
    allElements = ws.driver.find_elements(By.CSS_SELECTOR,"body *")
    l = []
    for element in allElements:
        href = element.get_attribute("href")
        if href and href.endswith(".pdf"):
            print(href, element.text)
            if len(element.text) > 0:
                l.append((element.text, href))
    for i in l:
        print(i)
    ws.driver.close()

