"""
pythonFile.py
Paul Talaga
Jan 22, 2020
Desc: Solution to Python Problem Set 1

"""
import math
import string

def hello(name, times = 1):
  for i in range(times):
    print("Hello {}".format(name))

def sumChars(string):
  sum = 0
  for i in range(len(string)):
    sum += ord(string[i])
  return sum

def isPrime(number):
  if number <= 1:
    return False
  for i in range(2,int(math.sqrt(number)) + 1):
    if number % i == 0:
      return False
  return True

def caesarEncrypt(string, offset):
  l = list(string) # convert to a list of characters so we can change
  for i in range(len(l)):
    if l[i] >= 'a' and l[i] <= 'z':
      l[i] = chr(((ord(l[i]) - ord('a') + offset) % 26) + ord('a'))
    elif l[i] >= 'A' and l[i] <= 'Z':
      l[i] = chr(((ord(l[i]) - ord('A') + offset) % 26) + ord('A'))
  return "".join(l)  # join will put that string (empty here) between each element

class SwearJar:
  def __init__(self):
    self.words = {'damn':0,'crap':0,'bloody':0,'bullshit':0,'pissed':0, 'shit':0}
    self.total_words = 0
    self.soap()

  def say(self, data):
    # Remove punctuation https://stackoverflow.com/questions/34293875/how-to-remove-punctuation-marks-from-a-string-in-python-3-x-using-translate
    translator = str.maketrans('', '', string.punctuation)
    data.translate(translator)
    data = data.lower()
    # Since the words could be wrapped in larger words, splitting
    # on space isn't an option, instead we use count
    for w in self.words.keys():
      self.words[w] += data.count(w)
    self.total_words += len(data.split(" "))


  def soap(self):
    for k in self.words.keys():
      self.words[k] = 0
    self.total_words = 0

  def reportCard(self):
    print("Total Words: {}".format(self.total_words))
    p_count = 0
    for k in self.words.keys():
      print("  {}: {}".format(k, self.words[k]) )
      p_count += self.words[k]
    if self.total_words != 0:
      print("That is {}% profanity.".format(int(p_count * 100 / self.total_words)))

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



