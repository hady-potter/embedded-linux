#shebang

# how to use this script
# first method
    # 1.put your {shebang} in first line like {/usr/bin/python3}
    # 2.in terminal write -> chmod +x open.py 
    # 3. run it like this -> ./open.py youtube
    # or like this -> ./open.py youtube google ...

# second method
    # python3 open.py youtube google 


import sys
import web

if len(sys.argv) < 2:
  print("missing args")
  print("use it like -> open youtube")
  print("or like -> open youtube google ...")
  exit(1)

links = sys.argv

# pop first element (script name) from links 
links.pop(0) 

# format link
for i in range(len(links)):
  links[i] = 'https://www.{}.com/'.format(links[i])


for link in links:
  web.firefox(link)


