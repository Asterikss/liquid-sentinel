from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

import LinksGetter


class WebScrapper:

    def __init__(self, url: str):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Edge()
        chrome_opt = Options()
        chrome_opt.add_argument("--disable-extensions")
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

