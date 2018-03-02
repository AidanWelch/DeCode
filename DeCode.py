import sys
if sys.version_info[0]>2:raw_input=input #Checks for Python3 adds raw_input
import os
import string
yesValues=["yes", "y", "yeah", "yep", "yea", "ok", "okay", "true"]

def FindFile():
	"Gets file from user and returns a string of the file" #Docstring
	while True:
		location = raw_input("Input your file's location: ")
		if not len(location): location= raw_input("You didn't type anything, try again: ")
		#Opens the file and finds it
		try:
			file = open(location, "r")
		except IOError as e:
			if str(e):print("Error Opening "+location+": "+str(e))
			else:print("Error Opening "+location)
			continue
		#File loaded succesfully
		print("Following will be the first 4 characters of " + os.path.basename(location) + ":")
		fileStr=file.read()
		print(fileStr[0:4])
		file.close()
		while True:
			answer = raw_input("Type Y if correct or N if false: ")
			if not answer: print("Nothing typed, try again."); continue
			if answer.lower() in yesValues: return fileStr
			else: break #Incorrect try again

def TallyChars(fileStr):
	"Counts each charecter in a string and returns a dictionary of the char and the count" #Docstring
	charCount = {}
	#Declaring Arrays and stuff ^
	for charCur in fileStr:
		if not (charCur in charCount):
			charCount[charCur]={"count": 1}
		else:
			charCount[charCur]["count"]+= 1
	#Character Tally^^^
	return charCount

def AdditionalCharInfo(charInfo):
	"Gets percentages for chars" #Docstring
	total = sum([charInfo[char]["count"] for char in charInfo])
	for char in charInfo:
		charInfo[char]["percent"]=float(int((float(charInfo[char]["count"])/float(total))*100000))/1000
	#converting to percentages and rounding/simplyifying number^
	#print charList
	#print "And here is the percentages of each:"
	#rint charPer
	#above is what i had before I improved the format
	#CompareChars(charList, charPer)
	return charInfo

def SortChars(unsortedList, percentCount):
	i = 0
	holdPer = []
	charList = []
	while i < len(unsortedList):
		if len(holdPer) == 0: #for the first value
			holdPer.append(percentCount[i])
			charList.append(unsortedList[i])
		elif percentCount[i] in holdPer: #if equal to any value
			index = holdPer.index(percentCount[i])
			holdPer.insert(index, percentCount[i])
			charList.insert(index, unsortedList[i])
		elif all(x < percentCount[i] for x in holdPer): #if greater than other values
			holdPer.append(percentCount[i])
			charList.append(unsortedList[i])
		elif all(x > percentCount[i] for x in holdPer): #if the lowest value
			holdPer.insert(0, percentCount[i])
			charList.insert(0, unsortedList[i])
		elif any(x < percentCount[i] for x in holdPer) and any(x > percentCount[i] for x in holdPer): #greater than some but less than others
			x = 0
			while percentCount[i] > holdPer[x]:#this starts low and works up but code won't continue until at the right point
				x = x + 1
			holdPer.insert(x, percentCount[i])
			charList.insert(x, unsortedList[i])
		i += 1
	return charList
def SortCharInfo(charInfo):
	"Sorts char info from least to greatest" #Docstring
	chars=list(charInfo.keys())
	charCounts=[charInfo[char]["count"] for char in list(charInfo.keys())]
	charPercents=[charInfo[char]["percent"] for char in list(charInfo.keys())]
	propertyArr=[chars, charCounts, charPercents]
	sortedArr=sorted([(propertyArr[0][i], propertyArr[1][i], propertyArr[2][i]) for i in range(len(chars))], key= lambda char: char[1])
	sortedDict={}
	for i in range(len(chars)):
		sortedDict[sortedArr[i][0]]={"count": sortedArr[i][1], "percent": sortedArr[i][2]}
	return sortedDict
"""
def CompareChars(charList, charPer):
#	englishLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Switch to string.ascii_uppercase
	charIncluded = []
	perIncluded = []
	for i in range(len(charList)):
		if charList[i] in string.ascii_letters and charList[i] not in string.ascii_letters:
			charIncluded.append(charList[i])
			perIncluded.append(charPer[i])
		else:
			print(charList[i] + " is not in the English alphabet")
	print(charIncluded)
	print(perIncluded)
	try:
		alphabet = open('/alphabet.txt', "r")
		alphabet.close()
	except IOError as e:
		print("Could not access 'alphabet.txt' please add that to this directory.")

#what I have so far in a soon to be tool to compare to the english alphabet and eventually de-cipher
"""
def Start():
	"Entry point" #Docstring
	print("\nD:\\Code initially by Aidan Welch\n")
	print("This is merely a tool to assist in deciphering, not an end all be all solution.  Meaning I can't guarantee this will help you.")
	raw_input("Press Enter(Return) to continue...")
	fileStr=FindFile()
	charInfo=TallyChars(fileStr)
	charInfo=AdditionalCharInfo(charInfo)
	charInfo=SortCharInfo(charInfo)
	charsCounted=len(list(charInfo.keys()))
	percentAccuracy=sum([charInfo[char]["percent"] for char in charInfo])
	print("Information about the "+str(charsCounted)+" chars counted from least to greatest")
	print("Note that percentage is ONLY accurate up to "+str(percentAccuracy)+"%")
	for char in charInfo:
		print("Char '%s': Count=%s, Percentage=%s" % (char, charInfo[char]["count"], charInfo[char]["percent"]))

Start()
