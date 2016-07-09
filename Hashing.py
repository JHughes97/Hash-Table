"""	Hash Table class
	Items are mapped to slots in the table using hash function
	If slot is taken, jumps through table by amount specified by double hash function
	Items can be searched for by using hash function again
"""

class HashTable:

	#object initialisation method
	def __init__(self,size):
		self.size = size                  #sets size of hash table
		self.table = [None]*size          #create list representing table
		self.probes = [None]*size         #create list which will hold collisions of each item inserted
		self.collisions = 0               #will record total number of collisions
		self.items = 0                    #will record total number of items

	#item insertion method
	def insert(self,input):
		index = self.getHashKey(input)			#get initial index to attempt
		jump = self.getDoubleHashKey(input)		#get amount of slots to jump	
		cols = 0								#cols will record number of collisions for item
		insert = input							#item being inserted

		while self.table[index] is not None:	#while an empty slot has not been found
			cols += 1
			self.collisions += 1
			if self.probes[index] < cols:		#if current item required less collisions than item being inserted, swap them
				temp = insert
				insert = self.table[index]
				self.table[index] = insert
				temp2 = cols
				cols = self.probes[index]
				self.probes[index] = temp2
			index += jump						#increment index by jump amount
			index = index%self.size             #modulo index by table size to avoid index out of bounds error

		self.table[index] = input				#insert item in table
		self.probes[index] = cols               #record number of collisions for this item
		self.items += 1

	#method to search for item
	def getSlot(self,input):
		index = self.getHashKey(input)				#get initial index value
		jump = self.getDoubleHashKey(input)			#get jump amount

		#search through table while current value is not None and item is not found
		#if index comes to an empty slot, the item is not in the table
		while self.table[index] != None and self.table[index] != input:
			index += jump
			index = index%self.size

		#print whether the item is in the table or not
		if self.table[index] is None:
			print("The word {} is not in HashTable".format(input))
		else:
			print("The word {} was found in slot {} of the HashTable".format(input,index))

	#function to get hash key value
	def getHashKey(self,input):
		key = 0

		for i in input:				#loop through string...
			key += ord(i)			#adding ascii value of current character,
			key += key<<10			#adding current value left shifted 10
			key ^= key>>6			#XORing with current value right shifted 6

		key += key<<3			#add on current value left shifted 3
		key ^= key>>11			#xor with current valud right shifted 11
		key += key<<15			#add current value left shifted 15

		return abs(key%self.size)		#return absolute value of hash key moduloed by size of table

	#function to get double hash key value (jump distance)
	def getDoubleHashKey(self,input):
		key = 0

		for i in range(len(input)):				#loop through string...
			key ^= ord(input[i])*(7**i)			#XORing with ascii value of current character times 7 to the power of index 

		return abs(key%self.size)		#return absolute value of key modulo size

	#method to return total number of collisions
	def collisions(self):
		return self.collisions

	#method which returns word at specified slot
	def getWord(self,num):
		return self.table[num]

	#method with returns size of table
	def size(self):
		return self.size

	#method which returns amount of items in table
	def itemAmount(self):
		return self.items

	#method which prints out items in table
	def printTable(self):
		for i in range(self.size):
			if self.table[i] is not None:
				print("Slot {} : {}\t-\tCollisions : {}".format(i,self.table[i],self.probes[i]))
		print("Table Size = {}".format(self.size))
		print("Number of Words = {}".format(self.items))
		print("Total Collisions = {}".format(self.collisions))

	#method which deletes specified items
	def delete(self,input):
		index = self.getHashKey(input)				#get initial index
		jump = self.getDoubleHashKey(input)			#get jump amount

		while self.table[index] != None and self.table[index] != input:		#loop while slot not empty and item not found
			index += jump
			index = index%self.size

		#print whether deletion was successful
		if self.table[index] is None:
			print("Word is not in the table")
		else:
			self.table[index] = None
			print("Word deleted from table")