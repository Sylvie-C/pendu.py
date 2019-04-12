""" --------------------------------------- """
"""             JEU DU PENDU                """ 
""" --------------------------------------- """
""" PJ:fichiers functions.py et data.py  """
""" --------------------------------------- """

# !/usr/bin/python3.5
# -*-coding:<Utf-8>-*-
from functions import *
from pickle import Pickler, Unpickler
from re import sub  # use of "sub" function in regular expression module for chain treatment
from os import remove # to remove data file at end of game

print ("\nBonjour brave joueur ! \nBienvenue dans le jeu du pendu ! \nTu dois trouver le mot caché ... ou tu seras pendu !!!\nFais ta prière, cowboy, et bonne chance !")

rep = "O"
name = ""

# new game initialization by data file removal
try : 
	remove("data.py") # if error thrown (meaning if data file doesn't exist), continue
except : 
	pass

# ------- Game beginning

name = input("\nSi tu es toujours là, saisis ton nom : ")

dicoScores = { name : 0 } # dic object key=player's name : value=score

# Scores object stored in "scores.txt" file : 
with open("scores.txt","wb") as scoresFile : 
	pickler = Pickler(scoresFile)
	pickler.dump(dicoScores)


# --- loop for new game ----
while rep=="O" or rep=="o" : 
	counter = 0 
	hiddenWord = pickAword()
	print ("\nLe mot caché contient " , len(hiddenWord) , " lettres. \nIndice : les accents ne comptent pas.")
	
	rounds = len(hiddenWord)*2 # the player has 2 times the hidden word length of chances to find it
	print("\nTu as " , rounds , " essais pour le trouver.")
	
	# lettersFound = results after player's input
	lettersFound = str(hiddenWord)  # copy of hiddenWord
	lettersFound = sub(".","*",lettersFound)  # every letters replaced with "*"
	
	# data file to exchange and compare data, in order to update result of player's input
	with open("data.py","x") as dataFile : # open and creates writeable data file
		dataFile.write(lettersFound) # writes letters found (none here) in data file

	# while rounds left or player has not found the hidden word
	while counter<rounds and (lettersFound != hiddenWord) : 
		counter +=1
		letter = input("\nSaisir une lettre : ")
		
		letter = strTests(letter) # Correct input tests
		
		letter = noAccents(letter) # no accents and to upper case
		
		occurr = hiddenWord.count(letter) # number of letter typed by player occurrences in hidden word

		# Game results while player hasn't won and still rounds left
		if (occurr > 0) :  # if there is a letter typed by player in hidden word
			print("\nIl y a " , occurr , letter , " dans le mot caché.\nIl te reste " , rounds-counter , " essais.")	
			
			findLetter(letter,lettersFound,hiddenWord)  # update and store result in data file
			with open("data.py") as dataFile : 
				lettersFound = dataFile.read()
			print(lettersFound)
		elif occurr == 0 : 
			print("\nIl n'y a pas de " , letter , " dans le mot caché.\nIl te reste " , rounds-counter , " essais.")
			print(lettersFound)
			
	# out of "while counter<rounds and (lettersFound != hiddenWord)" loop (if player has won or no more rounds left)
	if (counter>rounds) : 
		print("Tu as atteint les " , rounds , " essais. C'est perdu. Le mot caché était " , hiddenWord , ".\
	\nLa sentence est prononcée : tu seras pendu !!! Ha Ha Ha Ha Haaaaaaa !!! ")
	else : 
		with open("scores.txt","rb") as scoresFile : 
			unpickler = Unpickler(scoresFile)
			score = unpickler.load()	 # scores dictionary extraction from file

			totalScore = score[name] 
			print("Score précédent : " , totalScore)  # check value extracted from file

			totalScore += (rounds-counter) # add new score to value
			score.update({name : totalScore}) # add new name:score pair to others in dictionary
		
			print("Bravo ! Tu as trouvé en " , counter , " essai(s) et tu gagnes donc " , rounds-counter, " points.\nTon nouveau score est de " , score[name] , " points.")
		
		with open("scores.txt","wb") as scoresFile : 
			pickler = Pickler(scoresFile) 
			pickler.dump(score)   # save updated dictionary back to file

# ------- End of game ----------
	print ("\nRejouer (O/N) ?")
	rep = input()
	remove("data.py") # data file removal

print ("Tu t'en vas déjà ? Trouillard ! \nMerci d'avoir joué, au revoir ! ;-) ") # fin du jeu





