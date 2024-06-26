from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

names = []
params = []
return_types = []


# open file
src = open('docs/html/test_8h.html', 'r')

# create soup object
soup = BeautifulSoup(src, 'lxml')

# find return type
return_type = soup.find_all('td', {"class":"memItemLeft"}) #done

# find function signature
function_signature = soup.find_all('td', {"class":"memItemRight"})


names_and_params = []
for i in function_signature:
  names_and_params.append((i.text))


for i in names_and_params:
  name, param = i.split(' ', 1)
  names.append(name)
  params.append(param)

for i in return_type:
  return_types.append(i.text)


file_list = [return_types, names, params]
exported = zip_longest(*file_list)


with open('file.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(['return type', 'name', 'params'])
  writer.writerows(exported)


print('Done')
