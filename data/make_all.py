import json
import csv

odata = open("data_temp-1.json")
d = json.load(odata)
odata.close()

empty = '..'

#emp_pop_ratio Employment ratio
#gender_wage_gap Gender Wage Gap 
#maternity_parental_leave Maternity Parental Leave (had to add else for empty)
#maternity_weeks Maternity Weeks
#parliament_seats Parliament Seats
#senior_managers Senior Managers
#youth_unemployment Youth Unemployment (had to add else for empty)

with open('senior_managers.csv', 'r') as csv_file:
  csv_r = csv.reader(csv_file)
  #clean up the header
  h = csv_r.next()
  del h[0] 
  h.pop()
  for row in csv_r:
    c = row.pop(0)
    row.pop()
    for i, yr in enumerate(h):
      for year, o in d.iteritems():
        if year == yr:
          if row[i] != empty:
            d[year][c]["Senior Managers"] = float(row[i])

ndata = open("data_temp-1.json", "w")
ndata.write(json.dumps(d, separators = (',', ':')))
ndata.close()
