
# !/usr/bin/python3.5
# -*-coding:<Utf-8>-*-

""" --------- FONCTIONS POUR LE JEU DU PENDU ---------- """

# Modules et classes appelés par les fonctions
from random import randrange
from pickle import Pickler, Unpickler
from re import sub


def noAccents(word) : 
	"""Function to remove word accents and put it to upper case. 
			Returns updated word."""
	word = word.upper()
	
	regexA = "[ÀÂ]"
	regexE = "[ÉÈÊË]"
	regexI = "[ÏÎ]"
	regexO = "[ÔÖ]"
	regexU = "[ÛÙ]"
	
	word = sub(regexA,"A",word)
	word = sub(regexE,"E",word)
	word = sub(regexI,"I",word)
	word = sub(regexO,"O",word)
	word = sub(regexU,"U",word)
	
	return word


def strTests(letter) : 
	""" Function to test string received as parameter. 
			The string must be just 1 letter (type str) and not nothing. 
			Returns the correct string. """
	while True : # force input while errors 
		try : 
			assert len(letter) == 1 # cast error if string length is not exactly 1 letter
			if (letter.isalpha() == False) : raise TypeError # cast error if not aphabetic str
		except AssertionError : 
			letter = input("\nTu as saisi plus d'un caractère ou rien du tout. Recommence :  ")
		except TypeError : 
			letter = input("\nTu n'as pas saisi une lettre. Recommence : ")
		else : 
			break # if no errors thrown, out of loop
	return letter


def pickAword() : 
	"""Function to pick a random word in a custom file.
	The function extracts the words from the file,
	stores them in a list, selects a random integer,
	used as index to return the word."""	
	with open ("dico.txt") as fichier :  
		contenu = fichier.read()
		contenu = contenu.split() # words in file splitted at whitespaces or new line sep and stored in List object
	
	index = randrange(0,len(contenu))
	
	return contenu[index]


def findLetter(letter,result,solution) : 
	""" Function to update result and store it in data file. 
			Returns the updated result (letters found). """

	# regular expression construction : not letters found
	regex = "[^" + letter  # regex = [^letter
	for x in result :   # regex = [ ^ letter + already found letters in word
		if (x != "*") : regex += x
	regex += "]"			# regex = [ ^ letter + already found letters ]
	
	# replace not letters found with "*" in "solution" (not modified with "sub" function) and store result in "word"
	result = sub(regex,"*",solution) 

	# storage of new result in data file
	with open("data.py","w") as dataFile : 
		dataFile.write(result)   # updated found letters word stored in data file
		



# to test and independently execute functions.py file
if __name__ == "__main__" : 
	newresult = findLetter("I","L*B*RT*","LIBERTE")
	print(newresult)
	
	
	
	
	
	

