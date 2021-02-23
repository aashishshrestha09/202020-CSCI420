'''
Name: Paul Talaga
Date: 2-18-2021
Desc: Threading demo.

    https://docs.python.org/3/library/threading.html

'''

import threading
import time

def doStuff():
  for i in range(1,10):
    str = "Snow is "
    for x in range(i):
      str += " awesome"
    str += "!"
    print(str)
    time.sleep(0.5)

threading.Thread(target=doStuff).start()

print("I'm here")
time.sleep(1.0)
print("Or am I here?")


