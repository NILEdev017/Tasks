#QUESTION 1
def evenandodd(arr):
	oddsum = 0 # to store the addtion of all the odd numbers
	evensum = 0 # to store the addtion of all the even numbers

	for i in arr:		 
		if i % 2 == 0:  
			evensum += i # for each item in the array if it's completely divisible by 2 then add it to the even sum
		else:
			oddsum += i # otherwise add it to the odd sum


	return [evensum, oddsum] # return an array of the even sum and the odd sum


onetotwenty = [i for i in range(1, 21)] # create a list of numbers from 1 to 20

win = evenandodd(onetotwenty) # call the function
print(win)
