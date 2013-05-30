import csv

csv_file = open('women_labor-0.csv', 'w')
new_csv = csv.writer(csv_file)

with open('women_labor.csv', 'rw') as csvf:
  r = csv.reader(csvf)
  for row in r:
    for i, c in enumerate(row):
      if c == "":
        row[i] = 0
    new_csv.writerow(row)

csv_file.close()


