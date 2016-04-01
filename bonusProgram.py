
print("Hi! Welcome to Problem Set 0!")

tOC = ["isEven","lengthofNumber", "sumDigits", "lessThanGiven", "factorialFinder", "isFactor", "allFactors", "isPrime", "isPerfect", "divEven"]

print("Table of Contents")

placeHolder = 0

for i in tOC:
	print(str(placeHolder) + ". " + tOC[placeHolder])
	placeHolder = placeHolder + 1

mode = int(input("What would you like to test? Type the number of the program."))

if mode == 0:
	number = input("Insert a number ")

	print(isEven(number))
	
if mode == 1:
	number = input("Insert a number ")

	print(lengthofNumber(number))
	
if mode == 2:
	number = input("Insert a number ")

	print(sumDigits(number))
	
if mode == 3:
	number = input("Insert a number ")

	print(lessthanGiven(number))
	
if mode == 4:
	number = input("Insert a number ")

	print(factorialFinder(number))
	
if mode == 5:
	firstNumber = input("Insert a number ")
	secondNumber = input("Insert another number ")
	print(isFactor(firstNumber, secondNumber))
	
if mode == 6:
	number = input("Insert a number ")

	number = allFactors(number)

	print(number)

if mode == 7:
	number = input("Insert a number ")

	print(isPrime(number))

if mode == 8:
	number = input("Insert a number ")

	print(isPerfect(number))

if mode == 9:
	number = input("Insert a number ")

	print(divEven(number))
