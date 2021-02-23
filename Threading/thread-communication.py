'''
Name: Paul Talaga
Date: 2-18-2021
Desc: Threading demo.

'''

import threading
import time

word = "<>"
keep_going = True

def delay():
  global keep_going
  time.sleep(10)
  keep_going = False

def printStuff():
  global word
  global keep_going
  while keep_going:
    print("word is: {}".format(word))
    time.sleep(1)


t1 = threading.Thread(target=printStuff)
t1.start()

t2 = threading.Thread(target=delay)
t2.start()


t1.join()
t2.join()

print("All done!")
