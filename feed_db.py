import os
import json
from datetime import datetime
# import locale
# locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')

# date_str = "7 września 2023 r."
# date_obj = datetime.strptime(date_str, "%d %B %Y").strftime("%d-%m-%Y")
# print(date_obj)

directory = "llm_parsed_data"
polish_months = {
    'stycznia': 'January',
    'lutego': 'February',
    'marca': 'March',
    'kwietnia': 'April',
    'maja': 'May',
    'czerwca': 'June',
    'lipca': 'July',
    'sierpnia': 'August',
    'września': 'September',
    'października': 'October',
    'listopada': 'November',
    'grudnia': 'December'
}

for root, dirs, files in os.walk(directory):
    for filename in files:
        print("~~")

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
            data = data.replace(" r.", "")
            data = data.replace(" r", "")
            # aaa = data.replace("września", "September")
            not_found = True
            for pol_mon in polish_months.keys():
                if pol_mon in data:
                    data = data.replace(pol_mon, polish_months[pol_mon])
                    not_found = False
                    break
            print(data)
            if not_found:
                date_obj = datetime.strptime(data, "%d.%m.%Y").strftime("%d-%m-%Y")
            else:
                date_obj = datetime.strptime(data, "%d %B %Y").strftime("%d-%m-%Y")
            print(date_obj)
            data = {
                "bank_name": bank,
                "pivate_offer": indywidualni,
                "interest_rate": oprocentowanie,
                "date": date_obj
            }
            json_data = json.dumps(data, ensure_ascii=False)
            print(json_data)

        print("~~")
