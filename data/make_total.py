import csv

empty = '..'
countries = ['OECD average','Australia','Austria','Belgium','Canada','Czech Republic','Denmark','Finland','France','Germany','Greece','Hungary','Iceland','Ireland','Italy','Japan','Korea','Luxembourg','Mexico','Netherlands','New Zealand','Norway','Poland','Portugal','Slovak Republic','Spain','Sweden','Switzerland','Turkey','United Kingdom', 'United States']
years = [1970,2011]
d = {}

for country in countries:
  d[country] = {}
for country, o in d.iteritems():
  for year in years:
    d[country][year] = {
      'Employment',
      'Employment ratio',
      'Gender Wage Gap',
      'Maternity Weeks',
      'Parliament Seats',
      'Senior Managers'
        }

with open('employment_rate.csv', 'r') as emp_csv:
  emp_reader = csv.reader(emp_csv)
  h = []
  for row in emp_reader:
    print row 

'''
csv_file = open('women_labor.csv', 'w')
new_csv = csv.writer(csv_file)
columns =['Country', 'Year', 'Employment', 'Employment ratio', 'Gender Wage Gap', 'Maternity Weeks', 'Parliament Seats', 'Senior Managers']

new_csv.writerow(columns)
csv_file.close()
'''
