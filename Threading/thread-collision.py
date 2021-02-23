'''
Name: Paul Talaga
Date: 2-18-2021
Desc: An attempt of an incorrect global variable with multiple threads simultaneously
      incrementing.
      https://medium.com/python-features/pythons-gil-a-hurdle-to-multithreaded-program-d04ad9c1a63

'''

import threading
import time

NUM_THREADS = 100;
NUM_LOOPS = 1000000;

temp = 0

def doStuff(id):
  global temp
  for i in range(NUM_LOOPS):
    temp += 1
  print("Thread {} done".format(id))

# 
threads = []
for i in range(NUM_THREADS):
  threads.append( threading.Thread(target=doStuff, args=(i,)) )

for t in threads:
  t.start()

for t in threads:
  t.join()

print("Temp should be {}, but is {}".format(NUM_THREADS * NUM_LOOPS, temp))


