#Question 6

def arrayandint(arr, num):
	for i in arr: # 1st number in the array
		for j in arr: # 2nd number in the array
			for k in arr: # 3rd number in the array
				if i + j + k == num and i != j and i != k and j != i and j != k and k != i and k != j:
					# if the sum of all 3 unique numbers is equal to the number input into the function
					return [i, j, k] # then return all 3 numbers
		else:
			return -1 # otherwise return -1

numbers = [1, 2, 3, 4, 5, 6] # sample list
numm = 6 # test number

ans = arrayandint(numbers, numm)
print(ans)
