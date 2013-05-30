import csv
import json

odata = open("data_temp-1.json")
d = json.load(odata)
odata.close()

csv_file = open('women_labor.csv', 'w')
new_csv = csv.writer(csv_file)

#Columns
columns =['Country', 'Year', 'Employment', 'Employment ratio', 'Gender Wage Gap', 'Maternity Parental Leave', 'Maternity Weeks', 'Parliament Seats', 'Senior Managers', 'Youth Unemployment']
new_csv.writerow(columns)

#Data
for year, o in d.iteritems():
  for country, c in o.iteritems():
    try:
      c['Maternity Parental Leave']
    except KeyError:
      c['Maternity Parental Leave'] = ""
    r = [country, year, 
        c['Employment'],
        c['Employment ratio'],
        c['Gender Wage Gap'],
        c['Maternity Parental Leave'],
        c['Maternity Weeks'],
        c['Parliament Seats'],
        c['Senior Managers'],
        c['Youth Unemployment']
    ]
    new_csv.writerow(r)

csv_file.close()
