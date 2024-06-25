import csv

'''
Name, Age, Email
hady, 26 , hady.com
omar, 22 , omar.com
ahmed,25 , ahmed.com
'''

data = [
  ['Name', 'Age', 'Email'],
  ['hady', 26 , 'hady.com'],
  ['omar', 22 , 'omar.com'],
  ['ahmed', 25 , 'ahmed.com']
]


with open('file.csv', 'a') as f:
  writer = csv.writer(f)
  writer.writerows(data)


with open('file.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)