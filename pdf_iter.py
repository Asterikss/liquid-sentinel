import os
import pdfplumber

directory = 'bank_data'
bad_words: list[str] = ["wycof", "nieakt"]
length_max = 2000
# private_list = []
# bussiness_list = []

for root, dirs, files in os.walk(directory):
    for filename in files:
        whole_text = ""
        # Perform operations with the file
        # For example, print the file paths
        print(loc_path := os.path.join(root, filename))
        print(current_directory := os.path.join(root))
        if all(bad_words not in loc_path for bad_words in bad_words):
            whole_text = ""
            with pdfplumber.open(loc_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    whole_text += text
                    # type(text)
                    # print("here")
                    # print(text)
                    

            print("here")
            print(loc_path, "!!!!!")
            if "indywidualni" in loc_path:
                print(loc_path[loc_path.find("/")+1: loc_path.find("/", loc_path.find("/") + 1)])
                file_name = "parsed_data/" +  loc_path[loc_path.find("/")+1: loc_path.find("/", loc_path.find("/") + 1)] + "/indywidualni.txt"
                print(file_name)
                print(len(whole_text), "~!")
                if len(whole_text) < length_max:
                    print("here")
                    with open(file_name, 'w') as file:
                        file.write(whole_text)
                else:
                    print("here2")
                    whole_text = whole_text[whole_text.find("procentowan"):whole_text.find("procentowan")+length_max]
                    with open(file_name, 'w') as file:
                        file.write(whole_text)
            else:
                print("!!!!!!!!!!!!")
                print(loc_path[loc_path.find("/")+1: loc_path.find("/", loc_path.find("/") + 1)])
                file_name = "parsed_data/" +  loc_path[loc_path.find("/")+1: loc_path.find("/", loc_path.find("/") + 1)] + "/bussiness.txt"
                print(file_name)
                if len(whole_text) < length_max:
                    print("here3")
                    with open(file_name, 'w') as file:
                        file.write(whole_text)
                else:
                    print("here4")
                    whole_text = whole_text[whole_text.find("procentowan"):whole_text.find("procentowan")+length_max]
                    with open(file_name, 'w') as file:
                        file.write(whole_text)
                # with open(file_name, 'w') as file:
                    # file.write(whole_text)
                # bussiness_list.append(loc_path)

# updated_list = [desc for desc in l if not any(bad_word in desc[0] for bad_word in bad_words)]
print("----")
# print(private_list)
# print("----")
# print(bussiness_list)


