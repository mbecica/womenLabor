import csv
import json


d = {}

with open('continents.csv', 'r') as cont_csv:
  cont_read = csv.reader(cont_csv)
  for row in cont_read:
    d[row[0]] = row[1]

j = open('continents.json', 'w')
j.write(json.dumps(d, separators = (',', ':')))
j.close()
