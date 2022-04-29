import csv
filename="table_output0.csv"
string_to_look_for='Number of Coils'
fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
for i in fields:
    if i==string_to_look_for:
        pos=fields.index(i)
        break
data=[]
for i in range(len(rows)):
    data.append(rows[i][pos])
print(data)
    