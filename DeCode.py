import collections
import decimal
import sys
if sys.version_info[0]>2:raw_input = input #Checks for Python3 adds raw_input
import os
import re
import string
import json
yesValues=["yes", "y", "yeah", "yep", "yea", "ok", "okay", "true"]

def FindFile(location=None):
	"Gets file from user and returns a string of the file" #Docstring
	while True:
		if not location: location= raw_input("Input your file's location: ")
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
	charCount = collections.OrderedDict()
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
		charInfo[char]["percent"]=decimal.Decimal(int((decimal.Decimal(charInfo[char]["count"])/decimal.Decimal(total))*100000))/1000
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
	sortedDict=collections.OrderedDict()
	for i in range(len(chars)):
		sortedDict[sortedArr[i][0]]={"count": sortedArr[i][1], "percent": sortedArr[i][2]}
	return sortedDict
def SortCharPercents(charInfo):
	"Sorts char percents from least to greatest" #Docstring
	chars=list(charInfo.keys())
	charPercents=[charInfo[char]["percent"] for char in list(charInfo.keys())]
	propertyArr=[chars, charPercents]
	sortedArr=sorted([(propertyArr[0][i], propertyArr[1][i]) for i in range(len(chars))], key= lambda char: char[1])
	sortedDict=collections.OrderedDict()
	for i in range(len(chars)):
		sortedDict[sortedArr[i][0]]={"percent": sortedArr[i][1]}
	return sortedDict
def CompareChars(charInfo):
	"""
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
"""
	charInfo=SortCharPercents(collections.OrderedDict((char, charInfo[char]) for char in charInfo if char in string.ascii_letters))
	try:
		alphabetFile = open('./resources/alphabet.txt', "r")
	except IOError:
		print("Could not access 'alphabet.txt' please add that to this directory.")
	alphabetString=alphabetFile.read()
	alphabetFile.close()
	alphabetArr=re.findall(r"([A-Z])\s+(\d+.\d+)", alphabetString)
	alphabetInfo=collections.OrderedDict()
	for charArr in alphabetArr:
		alphabetInfo[charArr[0]]={"percent": decimal.Decimal(charArr[1])}
	alphabetInfo=SortCharPercents(alphabetInfo)
	"""
	if len(list(alphabetInfo.keys()))>len(list(charInfo.keys())):
		for char in alphabetInfo:
			if char not in charInfo:
				alphabetInfo.pop(char)
	else if len(list(alphabetInfo.keys()))<len(list(charInfo.keys()))
		for char in charInfo:
			if char not in alphabetInfo:
				charInfo.pop(char)
"""
	alphabetPercents=collections.OrderedDict()
	for char, info in alphabetInfo.items():
		if info["percent"] not in alphabetPercents: alphabetPercents[info["percent"]]=char
		else:alphabetPercents[info["percent"]]+=char
	alphabetMap=collections.OrderedDict()
	for char in charInfo:
		lastPercent=None
		for percent in alphabetPercents:
			if charInfo[char]["percent"]<percent: lastPercent=percent; continue
			alphabetMap[char]=alphabetPercents[lastPercent]
	return alphabetMap
	

#what I have so far in a soon to be tool to compare to the english alphabet and eventually de-cipher
def AnalyzeFile(inFile=None, outFile=None):
	"Entry point for analyzing a single file" #Docstring
	print("\nD:\\Code initially by Aidan Welch\n")
	print("This is merely a tool to assist in deciphering, not an end all be all solution.  Meaning I can't guarantee this will help you.")
	raw_input("Press Enter(Return) to continue...")
	fileStr=FindFile(inFile)
	charInfo=TallyChars(fileStr)
	charInfo=AdditionalCharInfo(charInfo)
	charInfo=SortCharInfo(charInfo)
	charsCounted=len(list(charInfo.keys()))
	percentAccuracy=sum([charInfo[char]["percent"] for char in charInfo])
	print("Information about the "+str(charsCounted)+" chars counted from least to greatest")
	print("Note that percentage is ONLY accurate up to "+str(percentAccuracy)+"%")
	if outFile:
		try: f=open(outFile, 'w')
		except IOError as e:
			if str(e):print("Error Opening "+outFile+": "+str(e))
			else:print("Error Opening "+outFile)
		else:
			jsonInfo='\t'.join(json.dumps(collections.OrderedDict((char, charInfo[char]["percent"]) for char in charInfo), indent=4).split(' '*4))
			f.write(jsonInfo)
			f.close()
	for char in charInfo:
		print("Char '%s': Count=%s, Percentage=%s" % (char, charInfo[char]["count"], charInfo[char]["percent"]))
helpString="""
D:\\Code initially by Aidan Welch

This is merely a tool to assist in deciphering encryption, not an end all be all solution.  Meaning I can't guarantee this will help you.

Command line options:
	--help (-h, -help):
		Prints this help and exits
	--analyze (-a):
		Analyzes a single file and converts it into a alphabet map,
		If '-o' is used with this, the program outputs the map as
		a .json if no other format is specified
	--output (-o):
		Specifies output file for any mode
	--compare (-c):
		Compares input file with file alphabet.format (format is json by default)
	--format (-f):
		Specifies format for output/alphabet files
		Formats are:
			json: json format
			txt: Char followed by percentage on next line
			xml: WIP
		Defaults to json
Examples:
	Compare a encrypted file, encrypted.txt, to a txt alphabet map, and output to decrypted.txt:
		%(filename)s --compare --format json --output decryted.txt encrypted.txt
	Same as above, with abbreviations:
		%(filename)s -c -f json -o decrypted.txt encrypted.txt
	You can mix shortened with full options:
		%(filename)s --format -o decrypted.txt encrypted.txt -c
	Analyze a file, dictionary.txt, into alphabet.txt
		%(filename)s -o alphabet.txt dictionary.txt --analyze
""" % {"filename": __file__}
argc=len(sys.argv)-1
inFile=None
fileFormat=None
outFile=None
argOptions=('-h', "-help", "--help", '-o', "--output", '-a', "--analyze", '-c', "--compare", 'f', "--format")
for i in range(1, argc):
	if sys.argv[i] in ('-h', "--help", "-help"): print(helpString); exit()
	elif sys.argv[i] in ('-o', "--output"):
		if i+1<=argc-1:
			i+=1
			outFile=sys.argv[i]
			continue
		else:
			print("-o/--output option used but no output specified!")
			exit()
	elif sys.argv[i] in ('-f', "--format"):
		if i+1<=argc-1:
			i+=1
			fileFormat=sys.argv[i]
			continue
	elif sys.argv[i] in argOptions: continue
	else:
		if not inFile: inFile=sys.argv[i]
		else: print("Unknown option '"+sys.argv[i]+"' ignored")

if '-a' in sys.argv or "--analyze" in sys.argv:
	AnalyzeFile(inFile= inFile, outFile= outFile)
elif '-c' in sys.argv or "--compare" in sys.argv:
	pass
else:
	print("No mode specified!\nUsage: "+__file__+" (--compare | --analyze) [--output, --format]")
