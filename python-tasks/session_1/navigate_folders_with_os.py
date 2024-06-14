import os

favFolders = [
  '/home/hady-potter/Dev',
  '/home/hady-potter/Book',
  '/home/hady-potter/Music',
]


user_input = int(input("Number: "))

if(user_input < len(favFolders)):
  os.popen(r"nautilus {}".format(favFolders[user_input]))