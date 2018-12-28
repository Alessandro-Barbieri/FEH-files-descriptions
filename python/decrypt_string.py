from itertools import cycle

class DecryptString():
	def __init__(self, cipher):
		self.cipher = cipher

	def decode(self, str):
		return bytes([m if m==c else m ^ c for m,c in zip(str, cycle(self.cipher))])