import csv

csvfile = open('1.csv', 'r', newline='')
reader = csv.DictReader(csvfile, dialect=csv.Sniffer().sniff(csvfile.read()))
csvfile.seek(0)
for row in reader:
    if int(row['New price']) < int(row['Old price']):
        print(row['Name'])
