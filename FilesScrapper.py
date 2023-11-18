import os
import shutil

class FilesScrapper:
    banks_dir = "banks"
    true_banks = "tr_banks"
    for bank_dir in os.listdir(banks_dir):
        print(bank_dir,":")
        file_path_b = banks_dir+"/"+bank_dir
        for type in ["person", "corporate"]:
            print("/t",type,":")
            file_path_ty = file_path_b + "/" + type
            for titled in ["titled", "nottitled"]:
                print("\t\t", titled, ":")
                file_path_ti = file_path_ty + "/" + titled
                print(file_path_ti)
                for pdf in os.listdir(file_path_ti):
                    print("\t\t\t", pdf, ":")
                    if "tab" in pdf and "procent" in pdf:
                        if not os.path.exists(true_banks):
                            os.mkdir(true_banks)
                        if not os.path.exists(true_banks+"/"+ bank_dir):
                            os.mkdir(true_banks+"/"+ bank_dir)
                        if not os.path.exists(true_banks+"/"+ bank_dir+"/"+type):
                            os.mkdir(true_banks+"/"+ bank_dir+"/"+type)
                        shutil.copy(file_path_ti+"/"+pdf, true_banks+"/"+bank_dir+"/"+type)

