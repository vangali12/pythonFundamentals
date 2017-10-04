## Multiples
# Pt. 1

def odds():
	for i in range (0, 1000):
		if i % 2 != 0 :
			print(i)

# Pt. 2

def fives():
	for i in range (5, 1000000):
		if i % 5 == 0 :
			print(i)

## Sum List

a = [1, 2, 5, 10, 255, 3]

def printSum(arr):
	sum = 0
	for i in range(0, len(arr)):
		sum += arr[i]
	print(sum)

## Average List

def printAvg(arr):
	sum = 0
	for j in range(0, len(arr)):
		sum += arr[j]
	print(sum/len(arr))

printAvg(a)