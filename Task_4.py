#Question 4
import re

patt0 = "[a-zA-Z]" # regex for letters only 
patt1 = "[0-9]" # regex for numbers only
patt2 = "[a-zA-z0-9]" # regex for letters and numbers
patt3 = "[a-zA-z0-9!@#$%^&*?]" # regex for letters, numbers and special characters

match1 = re.compile(patt0)
match2 = re.compile(patt1)
match3 = re.compile(patt2)
match4 = re.compile(patt3) # compile each pattern

def passval(password):
	if re.search(match1, password):
		return 0 # check if password matches pattern 0
	if re.search(match2, password):
		return 1 # check if password matches pattern 1
	if re.search(match3, password):
		return 2 # check if password matches pattern 2
	if re.findall(match1, password):
		return 3 # check if password matches pattern 3

ans = passval("Theman") # Example 1
ans2 = passval("123") # Example 2
ans3 = passval("4theMaN123") # Example 3
ans4 = passval("The$man123!#$") # Example 4

print(ans)
print(ans2)
print(ans3)
print(ans4)