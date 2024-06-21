import pyautogui as pg
from time import sleep

# while True:
#   sleep(0.5)
#   print(pg.position())

pg.press('win')
sleep(0.2)
pg.write('vscode')
sleep(0.2)
pg.press('enter')
sleep(0.2)

# go to extensions
pg.hotkey('ctrl', 'shift', 'x')
sleep(0.5)
# delete any text in search bar
pg.hotkey('ctrl', 'a')
sleep(0.5)
pg.hotkey('backspace')

sleep(1)
pg.write('c++ helper')

sleep(2)
pg.click(253, 221);

sleep(1)
pg.hotkey('ctrl', 'shift', 'x')
sleep(0.5)
pg.hotkey('ctrl', 'a')
sleep(1)
pg.hotkey('backspace')
sleep(0.2)
pg.write('c++ testmate')

sleep(2)
pg.click(253, 221);





