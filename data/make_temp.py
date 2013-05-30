import csv
import json

empty = '..'
countries = ['OECD average','Australia','Austria','Belgium','Brazil','Canada','Chile','China','Czech Republic','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Iceland','India','Indonesia','Ireland','Italy','Israel*','Japan','Korea','Luxembourg','Mexico','Netherlands','New Zealand','Norway','Poland','Portugal','Russian Federation','Slovak Republic','Slovenia','South Africa','Spain','Sweden','Switzerland','Turkey','United Kingdom', 'United States']
years = range(1970,2013)
d = {}

for year in years:
  d[year] = {}
for year, o in d.iteritems():
  for country in countries:
    d[year][country] = {
        'Employment': "",
        'Employment ratio': "",
        'Gender Wage Gap': "",
        'Maternity Weeks': "",
        'Parliament Seats': "",
        'Senior Managers': ""
        }


with open('employment_rate.csv', 'r') as emp_csv:
  emp_reader = csv.reader(emp_csv)
  #clean up the header
  h = emp_reader.next();
  del h[0]
  del h[17]
  for row in emp_reader:
    c = row.pop(0)
    code = row.pop()
    for i, yr in enumerate(h):
      for year, o in d.iteritems():
        if year == int(yr):
          if row[i] != empty:
            d[year][c]["Employment"] = float(row[i])

f = open('data_temp.json', 'w')
f.write(json.dumps(d, separators = (',', ':')))
f.close()

