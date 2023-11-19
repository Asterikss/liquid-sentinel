import json

jsons = []

with open("json_data/json_data.json", "r") as file:
    for line in file:
        jsons.append(json.loads(line))

output = []
for j in jsons:
    input_data = json.loads(j)
    bank_name = input_data.get("bank_name", "")
    interest_rate = input_data.get("interest_rate", "").replace(",", ".").replace("%", "")
    date = input_data.get("date", "")
    is_private_offer = input_data.get("private_offer", "")
    print(bank_name, interest_rate, date)
    to_model_str = "finances."
    # print(is_private_offer)
    # print(type(is_private_offer))
    if is_private_offer:
        to_model_str += "individual"
    else:
        to_model_str += "business"
    to_model_str += "depositoffer"
    output_data = {
    "model": to_model_str,
    "pk": 0,
    "fields": {
        "bank": 0,
        "name": bank_name,
        "description": "",
        "duration": None,
        "normal_interest_rate": float(interest_rate) if interest_rate else None,
        "date_start": date,
        "maturity": None,
        "created_at": "2023-11-18T23:57:36.989248Z",
        "conditions": ""
        }
    }

    # Convert the new dictionary to JSON string
    output_json = json.dumps(output_data)
    output.append(output_json)


with open("processed_json/processed_json.json", "w") as destination:
    for obj in output:
        json.dump(obj, destination)
        destination.write("\n")
