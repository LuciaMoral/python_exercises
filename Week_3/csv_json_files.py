import csv
import json

def csv_to_json(csv_filepath, json_filepath):
    data = {}
    with open(csv_filepath, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for rows in csv_reader:
            key = rows["name"]
            data[key] = rows

    with open(json_filepath, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data, indent=4))

csv_filepath = "names.csv"
json_filepath = "names.json"

csv_to_json(csv_filepath, json_filepath)

def json_to_csv(json_file, csv_file, data):
   with open(json_file, "r") as file:
       data = json.load(file)

   headers = data[0].keys()
   with open(csv_file, "w") as file:
       csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
       csv_writer.writeheader()
       for row in data:
           csv_writer.writerow(row)
