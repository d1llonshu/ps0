def isEven(number):
	number = int(number)
	answer = number / 2
	intAnswer = int(number / 2)
	if intAnswer == answer:
		return True
	else: 
		return False

def lengthofNumber(number):
	numberofTimes = 1
	total = 2
	while int(total) > 0.99:
		total = number / (10**numberofTimes)
		numberofTimes = numberofTimes + 1
	numberofTimes = numberofTimes - 1
	return numberofTimes

def sumDigits(number):
	size = lengthofNumber(number) - 1
	sum = 0
	placeHolder = 0
	list = []
	originalNum = number
	divide = 10**size
	while placeHolder <= size:
		number = originalNum
		if number < divide:
			list.append(number)
			break
		number = int(number / divide)
		originalNum = originalNum - number*divide
		list.append(number)
		placeHolder = placeHolder + 1
		divide = divide/10
	placeHolder = 0
	while placeHolder < len(list):
		sum = sum + list[placeHolder]
		placeHolder = placeHolder + 1
	return sum

def lessthanGiven(number):
	number = int(number)
	placeholder = number - 1
	sum = 0
	while placeholder > 0:
		sum = (placeholder) + sum
		placeholder = placeholder - 1
	return sum

def factorialFinder(number):
	number = int(number)
	placeholder = number
	sum = 1
	while placeholder > 0:
		sum = (placeholder) * sum
		placeholder = placeholder - 1
	return sum

def isFactor(firstNumber, secondNumber):
	sum = int(firstNumber) / int(secondNumber)
	intSum = int(sum)
	if intSum == sum:
		return True

	else:
		return False

def allFactors(number):
	listofFactors = []
	number = int(number)
	factor = 1
	while factor < number:
		answer = number / factor
		intAnswer = int(number / factor)
		if answer == intAnswer:
			listofFactors.append(factor)
		factor = factor + 1
	return listofFactors

def isPrime(number):
	listLength = len(allFactors(number))
	if listLength < 2:
		return True
	else:
		return False


def isPerfect(number):
	number = int(number)
	sum = allFactors(number)
	placeHolder = 0
	total = 0
	while placeHolder < len(sum):
		total = sum[placeHolder] + total
		placeHolder = placeHolder + 1
	if total == number:
		return True
	else:
		return False

def divEven(number):
	number = int(number)
	answer = number / sumDigits(number)
	intAnswer = int(number / sumDigits(number))
	if intAnswer == answer:
		return True
	else: 
		return False

