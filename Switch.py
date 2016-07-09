"""This class allows for the use of a
   switch statement"""

class switch(object):

	#initialisation method
	def __init__(self,value):
		self.value = value
		self.fall = False

	#allows iteration
	def __iter__(self):
		yield self.match
		raise StopIteration

	#returns whether case is true or false
	def match(self,*args):
		if self.fall or not args:
			return True
		elif self.value in args:
			self.fall = True
			return True
		else:
			return False