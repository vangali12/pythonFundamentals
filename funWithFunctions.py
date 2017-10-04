
def odd_even():
	for i in range (1, 2001):
		if (i % 2 != 0):
			print "Number is " + str(i) + ". This is an odd number."
		else:
			print "Number is " + str(i) + ". This is an even number."

# odd_even()

def multiply(box, fact):
	newList=[]
	for i in box:
		newList.append(i*fact)
	return newList

# print(multiply([5, 7, 3 ,2, 8, 7, 3], 5))

def hackerChallenge(arr):
	new_array = []
	for i in arr:
		curr = [1] * i
		new_array.append(curr)
	return new_array

# print(hackerChallenge(multiply([2, 4, 5], 3)))

