#Question 7
import math
def standarddev(arr):
	# formula of standard deviation is as follows:
	# x' is the mean, calculated by adding all the elements in the list and dividing by list length (n)
	# then for each number (x) in the list, the mean is subtracted from the number and the square is taken
	# the sum is added, divided by the length of the array minus 1 (n - 1)
	# and the squareroot everything is taken to get standard deviation
	# IN FORMULA FORM: sqrt(sum((x - x')**2)/(n - 1))

	mean, summ, bigsum = 0, 0, 0 # define variables 

	for i in arr:
		summ += i
		mean = (summ)/len(arr) # find the mean of the supplied list

	for i in arr:
		x = (i - mean)**2 # for each element find i - mean and then its square
		bigsum += x # sum for all the elements
		
	y = (bigsum)/(len(arr)-1) # divide sum by length of array - 1 


	return math.sqrt(y) # finally return square root for the final answer


nums = [82, 78, 65, 90, 12]
ans = standarddev(nums)

print(ans)
	



