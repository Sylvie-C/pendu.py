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

# ------- Game beginning

name = input("\nSi tu es toujours là, saisis ton nom : ")
name = name.upper()

rep = "O"	# reply to continue game or not

# SCORES file initialization

#	Check if scores file exists or not. If not, new player added with score = 0 (dict type object).
checkFile("scores.txt",name) # player {name:score = 0} stored

# if scores file exists and player exists -> game resumed by default (previous score updated at end of game)
# -> Check if player exists or not. If not, new player added to existing score file (update).

scoreData = readObjFile("scores.txt")
print(scoreData)

if name in scoreData : # if not new player ...
	if scoreData[name] > 0 : # if score > 0
		repResume = forceON (input("\nVeux-tu reprendre ta partie précédente ? (O/N)") ) # force answer O or N to choose resume game or not
		
		if repResume == "O" :  # player's choice = resume game (Oui)
			print ("Ton score actuel est de : " , scoreData[name] , " point(s).")
		else : # if player's choice = no game resume
			scoresUpdate("scores.txt",name,0) # reset score to 0 (update file scores with {player's name : 0})		
else : # if new player 
	scoresUpdate("scores.txt",name,0) # reset score to 0 (update file scores with {player's name : 0})


# Initialization of "data.py" file (remove it for new game)
try : 
	remove("data.py") # if error thrown (meaning if data file doesn't exist), continue
except : 
	pass


# --- loop for new game ----
while rep == "O" : 
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
	while (counter<rounds) and (lettersFound != hiddenWord) : 
		letter = input("\nSaisir une lettre : ")
		counter +=1
		
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
	if counter >= rounds : 
		print("Tu as atteint les " , rounds , " essais. C'est perdu. Le mot caché était " , hiddenWord , ".\nLa sentence est prononcée : tu seras pendu !!! Ha Ha Ha Ha Haaaaaaa !!! ")

	if (lettersFound == hiddenWord) : 
		scoresDict = readObjFile("scores.txt")	 # scores dictionary extraction from file

		score = scoresDict[name] # previous score extraction from dictionary
		score += (rounds-counter) # add new score to value

		scoresDict.update({name : score}) # update dictionnary with {player's name:score}
		
		print("Bravo ! Tu as trouvé en " , counter , " essai(s) et tu gagnes donc " , rounds-counter, " points.\nTon nouveau score est de " , scoresDict[name] , " point(s).")
		
		writeObjFile("scores.txt",scoresDict)   # save updated dictionary back to file

# ------- End of game ----------

	rep = forceON ( input("\nRejouer (O/N) ?") ) # force reply O or N to replay

	remove("data.py") # data file removal

print ("Tu t'en vas déjà ? Trouillard(e) ! \nMerci d'avoir joué, au revoir ! ;-) ") # fin du jeu



# CHECK UPDATE
scoresData = readObjFile("scores.txt")
print ("\nCheck file/dict updates : " , scoresData)





















