import os

directory = "llm_parsed_data"

for root, dirs, files in os.walk(directory):
    for filename in files:

        print(loc_path := os.path.join(root, filename))
        indywidualni = filename == "indywidualni.txt"
        bank = root[root.find("/")+1:]
        print(bank)
        print(indywidualni, "(indywidualni)")
        with open(loc_path, "r") as f:
            to_process = f.readlines()
            to_process = to_process[-1].strip()
            data = to_process[:to_process.find(";")]
            oprocentowanie = to_process[to_process.find(";") + 1: to_process.find("%") + 1].strip()
            print(oprocentowanie)
            print(data)
