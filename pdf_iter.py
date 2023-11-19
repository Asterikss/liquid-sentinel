'''
Iterate through collected PDFs, process text, shorten if too long
(After identifying potential location of the interest rate)
'''
import os
import pdfplumber
from typing import List

directory = "bank_data"
bad_words: List[str] = ["wycof", "nieakt"]
length_max = 4000

# Walk through all the files in bank_data directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        print("~~~~")
        # Collect information
        print(loc_path := os.path.join(root, filename))
        print(current_directory := os.path.join(root))

        # Check if any of the titels of the PDFs contain words that might
        # indicate that the information within them is outdated
        if all(bad_words not in loc_path for bad_words in bad_words):
            whole_text = ""
            with pdfplumber.open(loc_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    whole_text += text

            # Write the contents of the file to the correct destination
            # depending on the original location. Shorten if needed
            if "indywidualni" in loc_path:
                print(
                    "Bank:", 
                    loc_path[
                        loc_path.find("/")
                        + 1 : loc_path.find("/", loc_path.find("/") + 1)
                    ]
                )

                file_name = (
                    "parsed_data/"
                    + loc_path[
                        loc_path.find("/")
                        + 1 : loc_path.find("/", loc_path.find("/") + 1)
                    ]
                    + "/indywidualni.txt"
                )
                print("destination:", file_name)
                print("lenght of the document:", len(whole_text))

                if len(whole_text) < length_max:
                    print("kept as is (in private)")
                    with open(file_name, "w") as file:
                        file.write(whole_text)
                else:
                    print("shortened (in private)")
                    whole_text = whole_text[
                        whole_text.find("procentowan") : whole_text.find("procentowan")
                        + length_max
                    ]
                    with open(file_name, "w") as file:
                        file.write(whole_text)
            else:
                print(
                    "Bank:",
                    loc_path[
                        loc_path.find("/")
                        + 1 : loc_path.find("/", loc_path.find("/") + 1)
                    ]
                )
                file_name = (
                    "parsed_data/"
                    + loc_path[
                        loc_path.find("/")
                        + 1 : loc_path.find("/", loc_path.find("/") + 1)
                    ]
                    + "/bussiness.txt"
                )
                print("destination:", file_name)
                print("lenght of the document:", len(whole_text))

                if len(whole_text) < length_max:
                    print("kept as is (in business)")
                    with open(file_name, "w") as file:
                        file.write(whole_text)
                else:
                    print("shortened (in business)")
                    whole_text = whole_text[
                        whole_text.find("procentowan") : whole_text.find("procentowan")
                        + length_max
                    ]
                    with open(file_name, "w") as file:
                        file.write(whole_text)

        print("~~~~")
