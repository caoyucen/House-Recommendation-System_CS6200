import simplejson as json
import json
import csv

def read_csv_file():
    with open("./sampleData.json") as fp:
        for line in fp:
            print(line)

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

if __name__ == '__main__':
    # read_csv_file()
    csvFilePath = r'data.csv'
    jsonFilePath = r'data.json'
    csv_to_json(csvFilePath, jsonFilePath)








