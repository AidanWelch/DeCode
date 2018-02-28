import sys
if sys.version_info[0]>2:raw_input=input
import os
import string
def Start():
	print("\nD:\Code initially by Aidan Welch\n")

	print("This is merely a tool to assist in deciphering, not an end all be all solution.  Meaning I can't guarantee this will help you.")
	raw_input("Press Enter(Return) to continue...")
	FindFile()


def FindFile():
	location = raw_input("Input your file's location: ")
	while not len(location):
		location = raw_input("You didn't type anything, try again: ")
	#Opens the file and finds it
	file = open(location, "r")
	print("Following will be the first 4 characters of " + os.path.basename(location) + ":")
	fileStr=file.read()
	print(fileStr[0:4])
	file.close()
	while True:
		answer = raw_input("Type Y if correct or N if false: ")
		if answer.upper() == "Y":
			TallyChars(location)
			break
		elif answer.upper() == "N":
			FindFile()
			break
		else:
			continue


def TallyChars(fileStr):
	#must reopen file because everytime file is read it saves cursor position
	charList = []
	charCount = []
	#Declaring Arrays and stuff ^
	for charCur in fileStr:
		if((charCur in charList) == False):
			charList.append(charCur)
			charCount.append(1) 		
		else:
			currentPoint = charList.index(charCur)
			charCount[currentPoint] = charCount[currentPoint] + 1

	#Character Tally^^^
	print("Here are the characters counted:")
	print(str(charList))
	print("Here are the amount of times each appeared:")
	print(str(charCount))
	AdditionalCharInfo(charList, charCount)
	unanswered = False


def AdditionalCharInfo(unsortedList, unsortedCount):
	percentCount = []
	charList = [] #this is different from the old charCount and charList for simplification; this is sorted list
	charPer = [] #this is sorted percents
	total = sum(unsortedCount)
	for i in unsortedCount:
		percentCount.append(float(int((float(i)/float(total))*100000))/1000)
	#converting to percentages and rounding/simplyifying number^
	print("Here is the count converted to percentages:")
	print(percentCount)
	print("And this is the accuracy of the those percentages:")
	print(str(sum(percentCount)) + "%")
	charPer = sorted(percentCount)
	charList = SortChars(unsortedList, percentCount)
	print("Here are the characters sorted from least to greatest:")
	i = 0
	for i in range(len(charList)):
		print("'"+ str(charList[i]) + "'"+(' '*24)+ str(charPer[i]))
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
#	englishLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Switch to string.ascii_uppercase
	charIncluded = []
	perIncluded = []
	for i in range(len(charList)):
		if charList[i] in string.ascii_letters and charList[i] not in string.ascii_letters:
			charIncluded.append(charList[i])
			perIncluded.append(charPer[i])
		else:
			print charList[i] + " is not in the English alphabet"
	print charIncluded
	print perIncluded
	alphabet = open('/alphabet.txt', "r")
	alphabet.close()
#what I have so far in a soon to be tool to compare to the english alphabet and eventually de-cipher
"""
	

Start()