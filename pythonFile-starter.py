"""
pythonFile.py
--
Jan --, 2021
Desc: Solution to Python Problem Set 1

"""
import math
import string

# Fill in functions here!


if __name__ == "__main__":
  print("\nhello-function")
  print("\nHello Bob 1 time")
  hello("Bob")

  print("\nHello Bill 5 times")
  hello("Bill", 5)

  print("\nsumChars")
  print("65 = {}".format(sumChars("A")))
  print("130 = {}".format(sumChars("AA")))
  print("131 = {}".format(sumChars("AB")))
  print("131 = {}".format(sumChars("BA")))

  print("\nisPrime")
  print("True = {}".format(isPrime(7)))
  print("True = {}".format(isPrime(2)))
  print("False = {}".format(isPrime(6)))

  print("\ncaesarEncrypt")
  print("bcdea = {}".format(caesarEncrypt("abcdz", 1)))
  print("BCDEA = {}".format(caesarEncrypt("ABCDZ", 1)))
  print("bc?de. = {}".format(caesarEncrypt("ab?cd.", 1)))
  print("abcd = {}".format(caesarEncrypt("efgh", -4)))

  print("\nNo words given, should be all 0's.")
  sw = SwearJar()
  sw.reportCard()

  print("\nThis is a damn sentence.")
  sw = SwearJar()
  sw.say("This is a damn sentence.")
  sw.reportCard()
  sw.soap()
  print("\nSoap() called\n")
  print("This shITty homework will be the end of me.")
  print("The icecream in this damn town is bloody Shit.")
  sw.say("This shITty homework will be the end of me.")
  sw.say("The icecream in this damn town is bloody Shit.")
  sw.reportCard()

  print("\nNo words given, should be all 0's.")
  sw = SwearJar()
  sw.say("This damn assignment is bloddy bullshit.")
  sw.say("Python is a craptastic language that makes me pissed")
  sw.say("to program.")



