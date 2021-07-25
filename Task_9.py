#Question 9
def palindrome(palin):
	forward = [] # create an array for the word spelt forwards
	backward = [] # create an array for the word spelt backwards

	for i in palin:
		forward.append(i) # turn each alphabet in the input string to a letter in a list

	backward = [i for i in forward[::-1]] # reverse the forward list

	if forward == backward: # check if the string forwards and backwards are the same thing
		return("The string is a palindrome") # if yes, it's a palindrome
	else:
		return("The string is not a palindrome") # otherwise, it's not

ans = palindrome("Hound") # Example 1
ans2 = palindrome("123") # Example 2
ans3 = palindrome("123321") # Example 3
ans4 = palindrome("HannaH") # Example 4

# Note, the palindrome function is case-sensitive

print(ans)
print(ans2)
print(ans3)
print(ans4)