# Question 8
def howmany3s(n):
	string3s = [] # to hold all the numbers as strings
	final3s = [] # to hold all the numbers that have 3 in them
	count = 0 # to count each number that has a 3 in it

	listof3s = [i for i in range(0, n+1)]
	for i in listof3s:
		string3s.append(str(i)) # convert each number in the original list to a string
	
	for j in string3s:
		if '3' in j:
			count += 1 # if it contains 3 increase the number of count by one
			final3s.append(int(j)) # for each number with a 3 in the list, add it to the final list and turn it back into an integer
	return f"count: {count}, numbers: {final3s}" # output count and numbers in the intended format


aaa = howmany3s(35) # call the function
print(aaa)
