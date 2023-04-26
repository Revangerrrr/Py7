import csv

csvfile = open('rez.csv', 'r', newline='', encoding='utf8')
reader = csv.DictReader(csvfile, dialect=csv.Sniffer().sniff(csvfile.read()))
csvfile.seek(0)

school = '16'
class_num = '09'
results = []

for row in reader:
    login_split = row['login'].split('-')
    if login_split[2] == class_num and login_split[1] == school:
        name_split = row['user_name'].split()
        score = int(row['Score'])
        results.append((name_split[-1], score))

results.sort(key=lambda x: (-x[1], x[0]))

for result in results:
    print(result[0], result[1])
