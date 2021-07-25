# Question 5
def replacespace(uinput):
	newstring = uinput.replace(' ', '%20') #take an input and use the inbuilt replace function to turn all spaces to %20
	return newstring 

newans = replacespace("There are spaces in this string") # Example 1
newans2 = replacespace(" Look at all thesespaces      ") # Example 2
print(newans)
print(newans2)