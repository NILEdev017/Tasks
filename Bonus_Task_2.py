import string
alphabet = list(i for i in string.ascii_lowercase) # create a list of all the letters in the alphabet


def changeletter(s):
	vowels = ['a', 'e', 'i', 'o', 'u'] # list of vowels
	cons = [i for i in alphabet if i not in vowels] # list of consonants, for each i in alphabet that is not a vowel
	
	s1 = s.lower() # turn the input (s) and make it lower, stored in s1
	for i in s1: # for each alphabet in s1
		if i != " " and i not in vowels: # if the alphabet is not a space and is not a vowel
			cid = cons.index(i) # get the index of the letter
			s1 = s1.replace(i, cons[cid+1]) # replace the letter with the next letter in the list
	return s1 # return the new word


ans = changeletter("hello world")
print(ans)