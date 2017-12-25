import csv

csvfile = open('data/data-text.csv', 'rb')
reader = csv.DictReader(csvfile)

for row in reader:
    print row
