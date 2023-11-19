import os
import shutil


class FilesScrapper:
    @staticmethod
    def getAll():
        banks_dir = "banks"
        pdfs = []
        for bank_name in os.listdir(banks_dir):
            file_path_b = banks_dir + "/" + bank_name
            for type in ["person", "corporate"]:
                file_path_ty = file_path_b + "/" + type
                for titled in ["titled", "nottitled"]:
                    file_path_ti = file_path_ty + "/" + titled
                    for pdf in os.listdir(file_path_ti):
                        pdfs.append(file_path_ti + "/" + pdf)
        return pdfs

    @staticmethod
    def getBest():
        true_banks = "tr_banks"
        for pdf_full_path in FilesScrapper.getAll():
            parts = pdf_full_path.split("/")
            bank_name = parts[1]
            type = parts[2]
            titled = parts[3]
            pdf_name = parts[4]
            if "tab" in pdf_full_path and "procent" in pdf_full_path:
                if not os.path.exists(true_banks):
                    os.mkdir(true_banks)
                if not os.path.exists(true_banks + "/" + bank_name):
                    os.mkdir(true_banks + "/" + bank_name)
                if not os.path.exists(true_banks + "/" + bank_name + "/" + type):
                    os.mkdir(true_banks + "/" + bank_name + "/" + type)
                shutil.copy(pdf_full_path, true_banks + "/" + bank_name + "/" + type)

FilesScrapper.getBest()