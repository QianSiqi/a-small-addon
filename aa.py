import pyperclip
import os
while True:
    v = pyperclip.paste()
    if v == "hh":
        os.system('echo dabian')
        break