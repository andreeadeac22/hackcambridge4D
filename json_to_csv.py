import csv, json, sys

input = open(sys.argv[1])
data = json.load(input)
input.close()

with open("data.csv", "w") as file:

    output = csv.writer(file)

    output.writerow(data[0].keys())  # header row

    for row in data:
        output.writerow(row.values())
