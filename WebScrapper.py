import os

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib import request

import LinksGetter
from PDFManager import PDFManager


class WebScrapper:
    EDGE_PATH = 'edgedriver_win64/msedgedriver.exe'

    def __init__(self, url: str):
        self.driver = webdriver.Edge(executable_path=WebScrapper.EDGE_PATH)
        self.driver.get(url)

    # Cleaning text from illegal characters
    @staticmethod
    def clean(text: str):
        for illegal in "\n\\/:*?\"<>|":
            while illegal in text:
                text = text.replace(illegal, "")
        return text

        # Save all .pdf files from all urls in banks
    @staticmethod
    def try_save_best_PDFs_from_all_urls():
        banks = LinksGetter.BankData.get_banks_data_url_from_table()
        bank_dir = "banks" + "/"
        if not os.path.exists(bank_dir):
            os.mkdir(bank_dir)
        for bank in banks:
            if not os.path.exists(bank_dir + bank.bank_name):
                os.mkdir(bank_dir + bank.bank_name)
            for r in ["corporate", "person"]:
                if not os.path.exists(bank_dir + bank.bank_name + "/" + r):
                    os.mkdir(bank_dir + bank.bank_name + "/" + r)
                for t in ["titled", "nottitled"]:
                    if not os.path.exists(bank_dir + bank.bank_name + "/" + r + "/" + t):
                        os.mkdir(bank_dir + bank.bank_name + "/" + r + "/" + t)
            print(bank)
        i = 0
        for bank in banks:
            print(bank.bank_name + ":")
            for r in [bank.private_offer, bank.corporate]:
                try:
                    rodz = "person" if r == bank.private_offer else "corporate"
                    print(rodz + ":")
                    for link in r:
                        print(link)
                        ws = WebScrapper(link)
                        allElements = ws.driver.find_elements(By.CSS_SELECTOR, "body *")
                        for element in allElements:
                            try:
                                href = element.get_attribute("href")
                                if not (href and href.endswith(".pdf")):
                                    continue
                                if not "oprocent" in str(href).lower() and not "stop" in str(href).lower():
                                    if not "oprocent" in str(element.text).lower() or not "stop" in str(element.text).lower():
                                        continue
                                if "wycof" in str(href).lower() or "nieakt" in str(href).lower():
                                    if "wycof" in str(element.text).lower() or "nieakt" in str(element.text).lower():
                                        continue
                                code = str(href).split("/")[-1]
                                if (os.path.exists(
                                        bank_dir + bank.bank_name + "/" + rodz + "/" + "titled" + "/" + str(
                                                WebScrapper.clean(element.text)) + "_" + code) or
                                        os.path.exists(
                                            bank_dir + bank.bank_name + "/" + rodz + "/" + "nottitled" + "/" + code)):
                                    continue
                                if len(element.text) > 0:
                                    print(element.text, href)
                                    try:
                                        pdf_dir = bank_dir + bank.bank_name + "/" + rodz + "/" + "titled" + "/" + str(
                                            WebScrapper.clean(element.text)) + "_" + code
                                        request.urlretrieve(href, pdf_dir)
                                    except Exception:
                                        print("ERROR!", href, pdf_dir)
                                else:
                                    try:
                                        request.urlretrieve(href, "buf_pdf.pdf")
                                        tr = PDFManager.check_for_bad_word_in("buf_pdf.pdf",
                                                                              ["kredyt", "regulamin", "§"])
                                        if tr:
                                            if len(tr) > 0:
                                                continue
                                        print(element.text, href)
                                        pdf_dir = bank_dir + bank.bank_name + "/" + rodz + "/" + "nottitled" + "/" + code
                                        i += 1
                                        request.urlretrieve(href, pdf_dir)
                                    except Exception:
                                        print("ERROR!", href, pdf_dir)
                            except (selenium.common.exceptions.StaleElementReferenceException,
                                    selenium.common.exceptions.NoSuchElementException):
                                pass
                finally:
                    ws.driver.close()

    # Save all .pdf files from all urls in banks
    @staticmethod
    def save_all_PDFs_from_all_urls():
        banks = LinksGetter.BankData.get_banks_data_url_from_table()
        bank_dir = "banks" + "/"
        if not os.path.exists(bank_dir):
            os.mkdir(bank_dir)
        for bank in banks:
            if not os.path.exists(bank_dir + bank.bank_name):
                os.mkdir(bank_dir + bank.bank_name)
            for r in ["corporate", "person"]:
                if not os.path.exists(bank_dir + bank.bank_name + "/" + r):
                    os.mkdir(bank_dir + bank.bank_name + "/" + r)
                for t in ["titled", "nottitled"]:
                    if not os.path.exists(bank_dir + bank.bank_name + "/" + r + "/" + t):
                        os.mkdir(bank_dir + bank.bank_name + "/" + r + "/" + t)
            print(bank)
        i = 0
        for bank in banks:
            print(bank.bank_name + ":")
            for r in [bank.private_offer, bank.corporate]:
                try:
                    rodz = "person" if r == bank.private_offer else "corporate"
                    print(rodz + ":")
                    for link in r:
                        print(link)
                        ws = WebScrapper(link)
                        allElements = ws.driver.find_elements(By.CSS_SELECTOR, "body *")
                        for element in allElements:
                            try:
                                href = element.get_attribute("href")
                                if not (href and href.endswith(".pdf")):
                                    continue
                                print(element.text, href)
                                code = str(href).split("/")[-1]
                                if (os.path.exists(bank_dir + bank.bank_name + "/" + rodz + "/" + "titled" + "/" + str(
                                        WebScrapper.clean(element.text)) + "_" + code) or
                                        os.path.exists(
                                            bank_dir + bank.bank_name + "/" + rodz + "/" + "nottitled" + "/" + code)):
                                    continue
                                if len(element.text) > 0:
                                    try:
                                        pdf_dir = bank_dir + bank.bank_name + "/" + rodz + "/" + "titled" + "/" + str(
                                            WebScrapper.clean(element.text)) + "_" + code
                                        request.urlretrieve(href, pdf_dir)
                                    except Exception:
                                        print("EXCEPTION!", href, pdf_dir)
                                else:
                                    try:
                                        pdf_dir = bank_dir + bank.bank_name + "/" + rodz + "/" + "nottitled" + "/" + code
                                        i += 1
                                        request.urlretrieve(href, pdf_dir)
                                    except Exception:
                                        print("EXCEPTION!", href, pdf_dir)
                            except (selenium.common.exceptions.StaleElementReferenceException,
                                    selenium.common.exceptions.NoSuchElementException):
                                pass
                finally:
                    ws.driver.close()


if __name__ == "__main__":
    WebScrapper.try_save_best_PDFs_from_all_urls()