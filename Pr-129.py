import csv

data=[]
with open ("data1.csv", 'r') as f:
    v=csv.reader(f)
    for r in v:
        data.append(r)
headers=data[0]
plData=data[1:]
for l in plData:
    l[2]=l[2].lower()
plData.sort(key=lambda plData:plData[2])
with open("final.csv", 'a+') as f:
    w=csv.writer(f)
    w.writerow(headers)
    w.writerows(plData)

data2=[]
with open ("data2.csv", 'r') as f:
    v=csv.reader(f)
    for r in v:
        data2.append(r)
headers2=data[0]
plData2=data2[1:]
for l in plData2:
    l[2]=l[2].lower()
plData2.sort(key=lambda plData2:plData2[2])
with open("final.csv", 'a+') as f:
    w=csv.writer(f)
    w.writerow(headers2)
    w.writerows(plData2)