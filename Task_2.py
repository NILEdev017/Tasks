#QUESTION 2
def isitprime(i):
	factors = [j for j in range(2, i)] # list out all the factors excluding 1 and the number itself
	divcount = 0 # to count how many numbers can completely divide the input number

	if i > 1:
		for j in factors:
			if i % j == 0:
				divcount += 1 # if a number in the factors list can divide the input number without remainder then the divcount goes up
		if divcount > 0: # if the divcount is greater than 0 i.e if the number can be divided by things other than 1 and itself then
			return False # the number is not prime
		else: 
			return True # otherwise the number is prime

ans = isitprime(13) # call the function 
print(ans)