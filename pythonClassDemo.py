"""
pythonClassDemo.py
Paul Talaga
JFeb 6, 2020
Desc: Python class example

"""

class SwearJar:
	

	def __init__(self):
		print("__init__called")
		self.words = []

	def say(self, sentence = "Bob"):
		self.words.append(sentence)

	def reportCard(self):
		print(self.words)


if __name__ == "__main__":
	a = SwearJar()
	a.say("This is a damn sentence!")
	a.say("Yet another")
	a.say()
	a.reportCard()

	b = SwearJar()
	b.say()
	b.reportCard()