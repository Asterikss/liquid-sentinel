import os

import PyPDF2

from FilesScrapper import FilesScrapper


class PDFScrapper:
    @staticmethod
    def check_for_word(pdf_path, target_words):
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfFileReader(file)
                num_pages = pdf_reader.numPages

                for page_number in range(num_pages):
                    if page_number == 6:
                        return None
                    page = pdf_reader.getPage(page_number)
                    text = page.extractText()

                    l = [ill for ill in target_words if ill in text]
                    if len(l)>0:
                        return l
            return []
        except Exception:
            return None

pdfs = FilesScrapper.getAll()
# ills = ["kredyt", "regulamin"]
# for pdf_path in pdfs:
#     contains_word = PDFScrapper.check_for_word(pdf_path, ills)
#     if not contains_word:
#         print(f"Słowo '{ills}' nie wiadomo czy występuje w pliku PDF:",end=pdf_path)
#     elif len(contains_word)>0:
#         print(f"Słowo '{contains_word}' występuje w pliku PDF:",end=pdf_path)
#     else:
#         print(f"Słowo '{ills}' nie występuje w pliku PDF:",end=pdf_path)
#     print()
true_banks = "banks_txt"
for pdf in pdfs:
    try:
        text = ""
        with open(pdf, 'rb') as file:
            print(pdf)
            pdf_reader = PyPDF2.PdfFileReader(file)
            num_pages = pdf_reader.numPages
            parts = pdf.split("/")
            bank_name = parts[1]
            type = parts[2]
            titled = parts[3]
            pdf_name = parts[4]
            for page_number in range(num_pages):
                if page_number == 5:
                    break
                page = pdf_reader.getPage(page_number)
                text += page.extractText() + "\n"
        if not os.path.exists(true_banks):
            os.mkdir(true_banks)
        if not os.path.exists(true_banks + "/" + bank_name):
            os.mkdir(true_banks + "/" + bank_name)
        if not os.path.exists(true_banks + "/" + bank_name + "/" + type):
            os.mkdir(true_banks + "/" + bank_name + "/" + type)
        if not os.path.exists(true_banks + "/" + bank_name + "/" + type + "/" + pdf_name[:-4]+".txt"):
            new_pdf = true_banks + "/" + bank_name + "/" + type + "/" + pdf_name[:-4]+".txt"
        print(new_pdf)
        with open(new_pdf, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as ex:
        print("ERROR",ex, "in:", pdf)