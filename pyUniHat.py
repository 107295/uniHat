import sys

validatedNumber = [0];
years = 0;
yearWeights = [];
yearUnits = [];

def cls():
	print("\n" * 100)

def checkCmd(x):
	if(x == ".q"):
		print("Quitting...")
		sys.exit(0)
	elif(x == ".u"):
		print("Undoing...")

def checkNumber(y):
	while True:
		checkCmd(y)
		try:
			output = int(y)
			validatedNumber[0] = output
			break
		except:
			redo = input("Invalid- must be a positive integer! Try again: ")
			checkNumber(redo)
			break


# Program Begins
years = input("How many years is your course? ")
checkNumber(years)

print("Your course is", validatedNumber[0], "years long.")
years = validatedNumber[0]

for a in range(0, years):
	weighting = input("What is the weighting (percentage) of year %d? " %(a+1))
	checkNumber(weighting)
	yearWeights.append(validatedNumber[0])

print("Yearly weightings (in chronological order): ", yearWeights)

for a in range(0, years):
	units = input("How many assessed units are there in year %d? " %(a+1))
	checkNumber(units)
	yearUnits.append(validatedNumber[0])

print("", yearUnits)
