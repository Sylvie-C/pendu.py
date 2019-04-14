
# !/usr/bin/python3.5
# -*-coding:<Utf-8>-*-

""" --------- FUNCTIONS FOR GAME "LE PENDU" ---------- """

# MODULES - CLASSES CALLED
from random import randrange
from pickle import Pickler, Unpickler
from re import sub  # regex module
from os import path # to check if file existing



# FUNCTIONS

def writeObjFile (filePath,dataToWrite) : 
	"""	Function to write data in a file. 
			Passed parameters = file path, data to write. 
			Return : none. 
	"""
	with open(filePath,"wb") as dataFile : # open file as "w" creates it
			pickler = Pickler(dataFile)
			pickler.dump(dataToWrite) # save player's name + score = 0


def readObjFile (filePath) : 
	"""	Function to print and return an object stored in a file.
			Passed parameter : file path. 
			Return : object stored in file. """
	with open (filePath,"rb") as fileName : 
		unpickler = Unpickler (fileName)
		data = unpickler.load()
	return(data)


def checkFile(filePath,playerName) : 
	"""	Function to check if object storage file exists or not.
			If doesn't exist, the function creates it and adds dict object.
			with key:value pair of playerName:score=0. 
			Passed parameters : file path and player's name variable.
			No return. 
	"""
	if (path.isfile("scores.txt") == False) : # if file doesn't exist
		writeObjFile (filePath,{playerName:0}) # create it adding {player's name : score=0}



def scoresUpdate(filePath,playerName,score) : 
	"""	Function to update existing dict object type for players' scores, 
			within file object storage. 
			Passed parameters : file path, player's name, score, dictionnary name variable.
			Returns updated dictionnary. 
	"""
	# extract dict data from file
	data = readObjFile(filePath)
	
	# dict update
	data.update({playerName:score})		
	
	# dict storage back to file	
	writeObjFile(filePath,data)

			

def forceON(string) : 
	"""	Function to force player's input "O" or "N" or "o" or "n" (Oui / Non)
			Passed parameters : string.
			Returns True if "O", False if "N". 
	"""
	string = string.upper()
	while True : # force input while error thrown
		try : 
			assert (string == 'O' or string == 'N')
		except AssertionError : 
			string = input("\nSaisir O (oui) ou N (non) : ")
			string = string.upper()
		else : 
			break
	return string



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
			The string must be 1 letter type only and not nothing. 
			Returns the correct string. """
	while True : # force input while errors thrown
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


def pickAword(filePath) : 
	"""Function to pick a random word in a custom file.
	The function extracts the words from the file,
	stores them in a list, selects a random integer,
	used as index to return the word."""	
	with open (filePath) as fichier :  
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
	fileContent = readObjFile("scores.txt") # Tests readObjFile function
	print(fileContent)
	

