"""	Reads in dictionary and inserts words into Hash Table
	and prints total number of collisions
	User can print table or search for specified words
"""

#import hashtable class and switch class
from Hashing import HashTable
from Switch import switch

#open file containing words from dictionary
file = open("dictionary.txt", "r")

#create table, insert words, and print total number of collisions
print("Inserting words into HashTable...")
table = HashTable(430007)
for line in file:
	table.insert(line.replace("\n",""))
cols = table.collisions
print("Number of collisions = {}\n\n".format(cols))

#loop until user decides to exit
while True:
	x = int(input("\n1) Print all words\n2) Search for a word\n3) Quit\n"))

	#If user presses...
	#1..Print all words in table and print collisions of each word
	#2..Ask user to enter a word and search for that word
	#3..Exit loop
	stop = False
	for case in switch(x):
		if case(1):
			table.printTable()
			break
		if case(2):
			word = input("\nEnter word to be searched for:")
			table.getSlot(word)
			break
		if case(3):
			stop = True
			break
		if case():
			print("Invalid input\n")

	if stop:
		break
