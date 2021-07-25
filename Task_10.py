#Question 10
from collections import Counter

def whichishighest(st):
	final = Counter(st) # use counter function, to get dictionary of each letter in string as well as its number of occurrences

	for i in final:
		max_key = max(final) # in dictionary, pick the highest value

	for j in final:
		if final[j] == final[max_key]: # for the max value, if any other alphabet has similar number of occurrences 
			print({f'{j}: {final[j]}'}) # print out the key and its number of occurrences


ans = whichishighest("abbbcddddeeggggghijjjjjjjjjj") # Example 1
# ans2 = whichishighest("occassion") # Example 2

