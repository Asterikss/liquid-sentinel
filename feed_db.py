# Collect and process the data, so it is ready to be incorporated into a database
# Then write it to a file
import os
import json
from datetime import datetime

directory = "llm_parsed_data"

polish_months = {
    "stycznia": "January",
    "lutego": "February",
    "marca": "March",
    "kwietnia": "April",
    "maja": "May",
    "czerwca": "June",
    "lipca": "July",
    "sierpnia": "August",
    "września": "September",
    "października": "October",
    "listopada": "November",
    "grudnia": "December",
}

json_objects = []

# walk through llm_parsed_data directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        print("~~")

        loc_path = os.path.join(root, filename)
        is_private_offer = filename == "indywidualni.txt"
        bank = root[root.find("/") + 1 :]
        print(loc_path)
        print(bank)
        print(is_private_offer, "(is private offer)")

        # "Query" the last line of previously prepared files to get the date and the interest rate
        with open(loc_path, "r") as f:
            to_process = f.readlines()
            to_process = to_process[-1].strip()
            date = to_process[: to_process.find(";")]
            interest_rate = to_process[
                to_process.find(";") + 1 : to_process.find("%") + 1
            ].strip()
            print(interest_rate)
            print(date)
            date = date.replace(" r.", "")
            date = date.replace(" r", "")
            print(date)

            # process the data, depending on its form, so that it can be later easily parsable and queryable
            not_found = True
            for pl_month in polish_months.keys():
                if pl_month in date:
                    date = date.replace(pl_month, polish_months[pl_month])
                    not_found = False
                    break

            print(date)
            if not_found:
                date_obj = datetime.strptime(date, "%d.%m.%Y").strftime("%d-%m-%Y")
            else:
                date_obj = datetime.strptime(date, "%d %B %Y").strftime("%d-%m-%Y")
            print(date_obj)
            date = {
                "bank_name": bank,
                "pivate_offer": is_private_offer,
                "interest_rate": interest_rate,
                "date": date_obj,
            }
            json_data = json.dumps(date, ensure_ascii=False)
            json_objects.append(json_data)
            print(json_data)

        print("~~")

with open("json_data/json_data.json", "w") as destination:
    for obj in json_objects:
        json.dump(obj, destination)
        destination.write("\n")
