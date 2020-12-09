import csv

with open('kirara_book_chara.csv', encoding = 'utf8') as f:
    csvToDic = csv.DictReader(f)
    yml = open("test.yml", "w", encoding="utf-8")
    for row in csvToDic:
        name = row['Name'].replace(" ", "_")
        key = name.upper()
        yml.write(key + ': ' + row['Name_original'] + '\n')
        # print(row['Name'] + ' - ' + row['Name_original'])