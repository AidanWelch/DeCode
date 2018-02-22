import os

def Start():
	print ""
	print "D:\Code initially by Aidan Welch"
	print ""

	print("This is merely a tool to assist in deciphering, not an end all be all solution.  Meaning I can't guarantee this will help you.")
	raw_input("Press Enter(Return) to continue...")
	FindFile()


def FindFile():
	location = raw_input("Input your file's location: ")
	if len(location) < 1:
		print ("You didn't type anything")
		FindFile()
	else:
		 #Opens the file and finds it
		 file = open(location, "r")
		 print "Following will be the first 4 characters of " + os.path.basename(location) + ":"
		 print file.read(4)
		 unanswered = True
		 while unanswered == True:
		 	answer = raw_input("Type Y if correct or N if false: ")
		 	if answer.upper() == "Y":
		 		TallyChars(location)
		 		unanswered = False
		 	elif answer.upper() == "N":
		 		FindFile()
		 		unanswered = False
		 	else:
		 		unanswered = True


def TallyChars(location):
	#must reopen file because everytime file is read it saves cursor position
	file = open(location, "r")
	fileStr = file.read()
	charList = []
	charCount = []
	i = 0
	#Declaring Arrays and stuff ^
 	while i < len(fileStr):
		charCur = fileStr[i]
		if((charCur in charList) == False):
		 	charList.append(charCur)
		 	charCount.append(1) 		
		else:
		 	currentPoint = charList.index(charCur)
			charCount[currentPoint] = charCount[currentPoint] + 1
		
 		i = i + 1
 	#Character Tally^^^
 	print "Here are the characters counted:"
 	print charList
 	print "Here are the amount of times each appeared:"
 	print charCount
 	AdditionalCharInfo(charList, charCount, location)
	unanswered = False


def AdditionalCharInfo(unsortedList, unsortedCount, location):
	percentCount = []
	charList = [] #this is different from the old charCount and charList for simplification; this is sorted list
	charPer = [] #this is sorted percents
	total = sum(unsortedCount)
	i = 0
	while i < len(unsortedCount):
		percentCount.append(float(int((float(unsortedCount[i])/float(total))*100000))/1000)
		i = i + 1
	#converting to percentages and rounding/simplyifying number^
	print "Here is the count converted to percentages:"
	print percentCount
	print "And this is the accuracy of the those percentages:"
	print str(sum(percentCount)) + "%"
	charPer = sorted(percentCount)
	charList = SortChars(unsortedList, percentCount)
	print"Here are the characters sorted from least to greatest:"
	i = 0
	while i < len(charList):
		print "'"+ str(charList[i]) + "'                        " + str(charPer[i])
		i = i + 1
	#print charList
	#print "And here is the percentages of each:"
	#rint charPer
	#above is what i had before I improved the format
	#CompareChars(charList, charPer)

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
"""
def CompareChars(charList, charPer):
	englishLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	i = 0
	charIncluded = []
	perIncluded = []
	while i < len(charList):
		if charList[i].upper() in englishLetters and charList[i].upper() not in englishLetters:
			charIncluded.append(charList[i].upper())
			perIncluded.append(charPer[i])
		else:
			print charList[i] + " is not in the English alphabet"
		i += 1
	print charIncluded
	print perIncluded
	alphabet = open('/alphabet.txt', "r")
#what I have so far in a soon to be tool to compare to the english alphabet and eventually de-cipher
"""
	

Start()