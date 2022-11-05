#!/bin/python3

"""
FlagChecker V0.1
Todo :  Improve testFlag method with regular expressions
	Implement try/catch to handle bad args
"""

#libs
from sys import argv
from os import getpid,system

#flag
flag = argv[2]
print("[~] Your flag is:",flag)
print("[~] PID is:",getpid())

def testFlag(passw):
	special_characters = "\"'!@~éè#$%^&*()-+?_=,<>/"
	isStrong = True
	reason = "[!] flag doesn't match these critera : \n"
	upperChars = 0
	lowerChars = 0
	numChars = 0
	if(len(passw)<=12):
		isStrong = False
		reason+="\t-Not long enough (<12 characters)\n"
	for char in passw:
		if char.isupper():
			upperChars+=1
	if(upperChars==0):
		isStrong= False
		reason+="\t-There are no uppercase characters in your flag\n"
	for char in passw:
		if char.islower():
			lowerChars+=1
	if(lowerChars==0):
		isStrong = False
		reason+="\t-There are no lowercase characters in your flag\n"
	for char in passw:
		if char.isnumeric():
			numChars+=1
	if(numChars==0):
		isStrong = False
		reason+="\t-There are no numbers in your flag\n"
	if(char in special_characters for char in passw):
		a=""
	else:
		reason+="\t-There are no special chars in your flag\n"
		isStrong=False
	if(isStrong):
		print("[!] Your flag is strong enough !")
	else:
		print(reason)
	input("Press <ENTER> to quit program...")
#test flag
testFlag(flag)