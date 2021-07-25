#QUESTION 3
def isitprime(i):
	factors = [j for j in range(2, i)]
	divcount = 0 

	if i > 1:
		for j in factors:
			if i % j == 0:
				divcount += 1
		if divcount > 0: 
			return False 
		else: 
			return True 

def allprimenum(arr):
	primeonly = [] # to store the prime numbers

	for i in arr:		# for each item in the array if it's prime add it to the array
		if isitprime(i) == True:  # using the prime function from last time
			primeonly.append(i)	  # if the number is prime then it is added to the empty primeonly list

	return primeonly # return an array of the prime numbers


onetotwenty = [i for i in range(1, 21)] # create a list of numbers from 1 to 20 

win = allprimenum(onetotwenty) # call the function
print(win)